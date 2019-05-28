import os


def get_paths_list_from_folder(folder):
    """Gets all files in a given folder
    
    Parameters
    ----------
    folder : string
        folder in which search should be performed
    
    Returns
    -------
    paths: list
        relative paths for the given folder
    """
    names = os.listdir(folder)
    relative_paths = [os.path.join(folder, image_name) for image_name in names]
    return relative_paths