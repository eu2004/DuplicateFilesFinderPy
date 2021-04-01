import pickle
import os
import sys

# duplicate_files_map = pickle.load(open('GoFlex Home Backup_duplicated_files.pkl', 'rb'))
# duplicated_files_to_delete_csv = 'GoFlex Home Backup_duplicated_files_to_delete.csv'

duplicate_files_map = pickle.load(open('external_hdd_4TB_data02_duplicated_files.pkl', 'rb'))
duplicated_files_to_delete_csv = 'external_hdd_4TB_data02_duplicated_files.csv'
with open(duplicated_files_to_delete_csv, 'w', encoding="utf-8") as f_duplicated_files_to_delete_csv:
    for key, value in duplicate_files_map.items():
        if len(value) > 1:
            first_file = 1
            for duplicate_file in value:
                if first_file == 0:
                    f_duplicated_files_to_delete_csv.write(duplicate_file)
                    f_duplicated_files_to_delete_csv.write("\n")
                else:
                    first_file = 0

with open(duplicated_files_to_delete_csv, 'r', encoding="utf-8") as f_duplicated_files_to_delete_csv:
    Lines = f_duplicated_files_to_delete_csv.readlines()
    for line in Lines:
        file = line.strip()
        if os.path.exists(file):
            try:
                print("removing ", file)
                os.remove(file)
            except:
                except_type, value, traceback = sys.exc_info()
                print('error getting hash for: ', except_type, value, traceback)

