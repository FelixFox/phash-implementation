import os


def get_paths_list_from_folder(folder):
    names = os.listdir(folder)
    relative_paths = [os.path.join(folder, image_name) for image_name in names]
    return relative_paths