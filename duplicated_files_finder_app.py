import os.path
import sys
import FileHashHelper

if len(sys.argv) == 1:
    print('Directory path parameter is not set! Example of usage: duplicated_files_finder_app.py \'D:\\MyDocuments\' ')
    exit(1)

input_dir_path = sys.argv[1]
if os.path.isdir(input_dir_path):
    files_hashes_map = dict()
    try:
        files_hashes_map = FileHashHelper.get_folder_files_hashes(input_dir_path)
    except:
        except_type, value, traceback = sys.exc_info()
        print('error getting folder_files_hashes: ', except_type, value, traceback)
    duplicated_files_csv = os.path.basename(input_dir_path) + '_duplicated_files.csv'
    with open(duplicated_files_csv, 'w') as f_duplicated_files_csv:
        for key, value in files_hashes_map.items():
            if len(value) > 1:
                line = key + ", \"" + str(value) + "\"\n"
                f_duplicated_files_csv.write(line)
else:
    print(input_dir_path, ' is not a valid directory!')