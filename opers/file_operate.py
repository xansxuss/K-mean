import os


def get_file(path):
    file_list = []
    files =os.listdir(path)
    for file in files:
        if '.' in file:
            name = file.split('.')[0]
            file_list.append(name)
        else:
            continue
    return file_list

def check_path(path):
    if not os.path.isdir(path):
       os.makedirs(path) 