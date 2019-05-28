from similar_image_searcher import SimilarImagesSearcher
from argparse import ArgumentParser


def init_parser():
    """Just creates parser with a bunch of arguments.

    Returns
    -------
    parser: argparse.ArgumentParser
        ready object for parsing console arguments
    """
    parser = ArgumentParser(description="Test task for finding similar images")
    parser.add_argument(
        "-p", "--path", help="Path to folder with images", required=True)
    return parser


def find_similar_and_print_results(path):
    """Method created for performing a search between images in a given `path`
      to find similar ones

    Parameters
    ----------
    path : string
        path with images
    """
    searcher = SimilarImagesSearcher()
    searcher.search_similar_images_in_folder(path)
    searcher.print_results()


if __name__ == "__main__":
    parser = init_parser()
    args = parser.parse_args()
    find_similar_and_print_results(args.path)
