from os import listdir
from os.path import isfile, join


def get_files_in_folder(folder: str):
    '''
    This function allows to get all the files in a folder

    '''
    files = [(f, "file" if isfile(join(folder, f)) else "folder")
             for f in listdir(folder)]
    return dict(files)


folder = input('Folder absolute path: ')

print(get_files_in_folder(folder))
