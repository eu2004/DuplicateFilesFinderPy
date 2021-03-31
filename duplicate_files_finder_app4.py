import os.path
import pickle
import sys
from pathlib import Path
import json

import FileHashHelper

if len(sys.argv) == 1:
    print('Directory path parameter is not set! Example of usage: duplicate_files_finder_app.py \'D:\\MyDocuments\' ')
    exit(1)


def compute_file_hash(filepath):
    global except_type, value, traceback
    try:
        return FileHashHelper.get_file_hash(filepath)
    except:
        except_type, value, traceback = sys.exc_info()
        print('error getting folder_files_hashes: ', filepath, except_type, value,
              traceback)
    return 'error'


def get_file_size(filepath):
    global file_size, except_type, value, traceback
    file_size = -1
    try:
        file_size = os.stat(filepath).st_size
    except:
        except_type, value, traceback = sys.exc_info()
        print('error getting file size: ', filepath, except_type, value, traceback)
    return file_size


class DuplicatedFile:
    def __init__(self, filepath, filehash):
        self.file_path = filepath
        self.file_hash = filehash

    def __hash__(self):
        return hash(self.file_path)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.file_path == other.file_path and self.file_hash == other.file_hash


input_dir_path = sys.argv[1]

if os.path.isdir(input_dir_path):
    file_size_map = dict()
    file_hash_map = dict()
    for file_path in Path(input_dir_path).rglob('*'):
        if os.path.isfile(file_path):
            file_size = get_file_size(file_path)
            if file_size in file_size_map:
                duplicated_files_sizes_list = file_size_map[file_size]
                duplicated_files_sizes_list.append(DuplicatedFile(str(file_path), -1))
                for duplicated_file in duplicated_files_sizes_list:
                    if duplicated_file.file_hash == -1:
                        duplicated_file.file_hash = compute_file_hash(duplicated_file.file_path)
                    if duplicated_file.file_hash in file_hash_map:
                        duplicated_files_set = file_hash_map[duplicated_file.file_hash]
                        duplicated_files_set.add(duplicated_file.file_path)
                    else:
                        duplicated_files_set = set()
                        duplicated_files_set.add(duplicated_file.file_path)
                        file_hash_map[duplicated_file.file_hash] = duplicated_files_set
            else:
                duplicated_files_sizes_list = list()
                duplicated_files_sizes_list.append(DuplicatedFile(str(file_path), -1))
                file_size_map[file_size] = duplicated_files_sizes_list

    file_size_map.clear()
    del file_size_map

    duplicated_files_pkl = os.path.basename(input_dir_path) + '_duplicated_files.pkl'
    pickle.dump(file_hash_map, open(duplicated_files_pkl, 'wb'))
else:
    print(input_dir_path, ' is not a valid directory!')
