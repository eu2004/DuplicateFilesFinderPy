import os.path
import pickle
import sys
from pathlib import Path

import FileHashHelper

if len(sys.argv) == 1:
    print('Directory path parameter is not set! Example of usage: duplicate_files_finder_app.py \'D:\\MyDocuments\' ')
    exit(1)


class DuplicatedFile:
    def __init__(self, file_name, file_hash):
        self.file_name = file_name
        self.file_hash = file_hash


input_dir_path = sys.argv[1]
if os.path.isdir(input_dir_path):
    files_hashes_map = dict()
    duplicated_files_map = dict()
    for elem in Path(input_dir_path).rglob('*'):
        if os.path.isfile(elem):
            try:
                file_size = os.stat(elem).st_size
            except:
                except_type, value, traceback = sys.exc_info()
                print('error getting file size: ', except_type, value, traceback)
            if file_size in files_hashes_map:
                files_list = files_hashes_map[file_size]
                files_list.append(DuplicatedFile(str(elem), 0))
                for duplicated_file in files_list:
                    if duplicated_file.file_hash == 0:
                        file_hash = 'error'
                        try:
                            file_hash = FileHashHelper.get_file_hash(duplicated_file.file_name)
                            duplicated_file.file_hash = file_hash
                        except:
                            except_type, value, traceback = sys.exc_info()
                            print('error getting folder_files_hashes: ', except_type, value, traceback)
                    if duplicated_file.file_hash in duplicated_files_map:
                        duplicated_files_list = duplicated_files_map[duplicated_file.file_hash]
                        duplicated_files_list.append(duplicated_file.file_name)
                    else:
                        duplicated_files_list = list()
                        duplicated_files_list.append(duplicated_file.file_name)
                        duplicated_files_map[duplicated_file.file_hash] = duplicated_files_list
            else:

                files_list = list()
                files_list.append(DuplicatedFile(str(elem), 0))
                files_hashes_map[file_size] = files_list

    for key, value in duplicated_files_map.items():
        if len(value) <= 1:
            del key
            del value

    files_hashes_map.clear()
    del files_hashes_map

    duplicated_files_csv = os.path.basename(input_dir_path) + '_duplicated_files.pkl'
    pickle.dump(duplicated_files_map, open(duplicated_files_csv, 'wb'))
else:
    print(input_dir_path, ' is not a valid directory!')
