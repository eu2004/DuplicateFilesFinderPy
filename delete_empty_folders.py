import os.path
import sys

if len(sys.argv) == 1:
    print('Directory path parameter is not set! Example of usage: delete_empty_folders.py \'D:\\MyDocuments\' ')
    exit(1)

input_dir_path = sys.argv[1]
if not os.path.isdir(input_dir_path):
    print(input_dir_path, 'is not a directory!')
    exit(1)


class VerifiedFolder:
    def __init__(self, filepath, visited):
        self.file_path = filepath
        self.visited = visited


def delete_folder(current_folder_file_path):
    if len(os.listdir(current_folder_file_path)) == 0:
        try:
            print("deleting ", current_folder_file_path)
            os.rmdir(current_folder_file_path)
        except:
            except_type, value, traceback = sys.exc_info()
            print('error deleting folder: ', current_folder_file_path, except_type, value, traceback)


folders_to_verify = list()
verified_folder = VerifiedFolder(input_dir_path, False)
folders_to_verify.append(verified_folder)

while len(folders_to_verify) > 0:
    current_folder = folders_to_verify[len(folders_to_verify) - 1]
    if current_folder.visited:
        folders_to_verify.pop(len(folders_to_verify) - 1)
        delete_folder(current_folder.file_path)
    else:
        current_folder.visited = True
        content_of_current_folder = os.listdir(current_folder.file_path)
        if len(content_of_current_folder) == 0:
            folders_to_verify.pop(len(folders_to_verify) - 1)
            delete_folder(current_folder.file_path)
        else:
            current_folder_has_sub_folders = False
            for folder in os.listdir(current_folder.file_path):
                if os.path.isdir(os.path.join(current_folder.file_path, folder)):
                    current_folder_has_sub_folders = True
                    verified_folder = VerifiedFolder(os.path.join(current_folder.file_path, folder), False)
                    folders_to_verify.append(verified_folder)
            if not current_folder_has_sub_folders:
                folders_to_verify.pop(len(folders_to_verify) - 1)
