from os import listdir
from os.path import isfile, join


def get_files_in_folder(folder: str) -> dict:
    '''
    This function allows to get all the files in a folder

    '''
    files = [(f, "file" if isfile(join(folder, f)) else "folder")
             for f in listdir(folder)]
    return dict(files)


def print_elements_from_dict(dict: dict) -> None:
    for k, v in dict.items():
        print(f'name: {k}, type: {v}')


folder = input('Folder absolute path: ')

print_elements_from_dict(get_files_in_folder(folder))
