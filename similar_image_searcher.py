"""
Author: Anastasia Kriuchkovska
E-mail: staceyhooks0@gmail.com

"""

from PIL import Image
import numpy as np
from phash import PHash
from utils import get_paths_list_from_folder




class SimilarImagesSearcher:
    """Class for finding similar images in a given folder. It uses PHash algorithm.
    """
    def __init__(self):
        self.hasher = PHash()
        self.sorted_hash_results = None

    def get_distance(self, s1: np.array, s2: np.array):
        return np.count_nonzero(s1.flatten() != s2.flatten())

    def search_similar_images_in_folder(self, dataset_folder):
        images_paths = get_paths_list_from_folder(dataset_folder)
        image_paths_hashes_dict = self.__get_images_hashes(images_paths)
        comparison_results = {}
        for image_path, hash in image_paths_hashes_dict.items():
            compare_result = {}
            for image_path_to_compare, hash_to_compare in image_paths_hashes_dict.items():
                if image_path_to_compare != image_path:
                    compare_result[image_path_to_compare] = self.get_distance(
                        hash, hash_to_compare
                    )
            comparison_results[image_path] = compare_result

        self.sorted_hash_results = self.__sort_comparison_results(comparison_results)
        
    def __get_images_hashes(self, image_paths):
        image_paths_hashes_dict = {}
        for path in image_paths:
            image = Image.open(path)
            hash = self.get_image_hash(image)
            image_paths_hashes_dict[path] = hash
        return image_paths_hashes_dict


    def get_image_hash(self,image):
        hash = self.hasher.get_hash(image)
        return hash


    def __sort_comparison_results(self, comparison_results):
        sorted_hashes = {}
        for image_path, results in comparison_results.items():
            sorted_results = [(k, results[k]) for k in sorted(results, key=results.get)]
            sorted_hashes[image_path] = sorted_results
        return sorted_hashes


    def print_results(self):
        assert (self.sorted_hash_results is not None), "Comparison results are not computed yet.. Call self.search_similar_images_in_folder()"
        for image_path, res in self.sorted_hash_results.items():
            print(
                "for {} most similar are {}, {}, {}".format(
                    image_path, res[0], res[1], res[2]
                )
            )


searcher = SimilarImagesSearcher()
searcher.search_similar_images_in_folder("./dev_dataset")
searcher.print_results()

