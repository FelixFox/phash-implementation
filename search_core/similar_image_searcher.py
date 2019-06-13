"""
Author: Anastasia Kriuchkovska
E-mail: staceyhooks0@gmail.com

"""

from PIL import Image
import numpy as np
from .phash import PHash
from utils.fs import get_paths_list_from_folder
import os


class SimilarImagesSearcher:
    """Class for finding similar images in a given folder. It uses PHash algorithm.
    """

    def __init__(self):
        self.hasher = PHash()
        self.sorted_hash_results = None

    def get_distance(self, s1: np.array, s2: np.array):
        """
            Counts a distance between two image hashes. 
        Parameters
        ----------
        s1: np.array
            hash of the first image
        s2: np.array
            hash of the second image


        Returns
        -------
        count: int or array of int
            Number, representing distance between hashes
        """
        return np.count_nonzero(s1.flatten() != s2.flatten())

    def search_similar_images_in_folder(self, dataset_folder, threshold=20):
        """Performs searching similar images in a given dataset folder using distance threshold.

        Parameters
        ----------
        dataset_folder : string
            folder with dataset images, from which there will be chosen similar ones
        threshold : int, optional
            distance threshold used for comparing two images (smaller threshold means algorithm will     
            select more alike images for each one), by default 20
        """
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

        self.sorted_hash_results = comparison_results
        self.apply_threshold_to_result(threshold=threshold)

    def __get_images_hashes(self, image_paths):
        """Calculates hash for each image from given list of image paths.

        Parameters
        ----------
        image_paths : list of strings
            list with paths for each image

        Returns
        -------
        image_paths_hashes_dict : dict
            dict containing pairs {image_path:image_hash} 
        """
        image_paths_hashes_dict = {}
        for path in image_paths:
            image = Image.open(path)
            #print(f"Getting hash for {path} ...")
            hash = self.get_image_hash(image)
            image_paths_hashes_dict[path] = hash
        return image_paths_hashes_dict

    def get_image_hash(self, image):
        """Calculates a hash for the given image.
        
        Parameters
        ----------
        image : PIL.Image
            image data
        
        Returns
        -------
        hash: np.array
            binary hash for the given image
        """
        hash = self.hasher.get_hash(image)
        return hash

    def print_results(self):
        """Prints results from `self.sorted_hash_results` in the form of pair: image similar_image
        """
        pairs = []
        for image_path, res in self.sorted_hash_results.items():
            if len(res) > 0:
                for el in res:
                    pairs.append(tuple(sorted([image_path, el[0]])))
        pairs = set(pairs)
        for pair in pairs:
            print("{} {}".format(pair[0], pair[1]))

    def apply_threshold_to_result(self, threshold):
        """Removes images for each image in self.sorted_hash_results due to their distances. If distance < threshold,
        then image is considered as not similar to given one.
        
        Parameters
        ----------
        threshold : int
            distance threshold
        """
        for image_path, res in self.sorted_hash_results.items():
            most_similar = []
            for path, dintance in res.items():
                if dintance < threshold:
                    most_similar.append((path, dintance))
            self.sorted_hash_results[image_path] = most_similar
