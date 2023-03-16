import os

def solve_dir(dirname:str)->str:

    if not os.path.exists(dirname):
        os.mkdir(dirname)
    
    return os.path.abspath(dirname)


def solve_path(path:str, parent=None)->str:

    if parent:
        parent = solve_dir(parent)
        path = os.path.join(parent, path)

    return os.path.abspath(path)

def get_extension(file_path:str)->str:

    _, file_extension = os.path.splitext(file_path)

    return file_extension

def lst_files(folder:str, extensions:list)->list:

    #more performatic
    extensions = set(extensions)

    return [file for file in os.listdir(folder)
            if get_extension(file) in extensions]