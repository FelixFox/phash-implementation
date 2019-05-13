from similar_image_searcher import SimilarImagesSearcher
from argparse import ArgumentParser


def init_parser():
    parser = ArgumentParser(description="Test task for finding similar images")
    parser.add_argument("-p", "--path", help="Path to folder with images", required = True)
    return parser


def find_similar_and_print_results(path):
    searcher = SimilarImagesSearcher()
    searcher.search_similar_images_in_folder(path)
    searcher.print_results()


if __name__ == "__main__":
    parser = init_parser()
    args = parser.parse_args()
    find_similar_and_print_results(args.path)

