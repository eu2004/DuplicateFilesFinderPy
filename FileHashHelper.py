import hashlib
import os.path
from pathlib import Path
import sys


def get_file_hash(file_path):
    return hashlib.sha512(open(file_path, 'rb').read()).hexdigest()


def get_folder_files_hashes(folder_path):
    duplicated_files_map = dict()
    for elem in Path(folder_path).rglob('*'):
        if os.path.isfile(elem):
            file_hash = 'error'
            try:
                file_hash = get_file_hash(elem)
            except:
                except_type, value, traceback = sys.exc_info()
                print('error getting hash for: ', elem, except_type, value, traceback)
            if file_hash in duplicated_files_map:
                duplicated_files_list = duplicated_files_map[file_hash]
                duplicated_files_list.append(str(elem))
            else:
                duplicated_files_list = list()
                duplicated_files_list.append(str(elem))
                duplicated_files_map[file_hash] = duplicated_files_list

    return duplicated_files_map
