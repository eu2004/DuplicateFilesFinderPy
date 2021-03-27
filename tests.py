import json
import pickle


# duplicated_files_keys_csv = '12TB_._duplicated_files_keys.csv'
# duplicated_files_values_csv = '12TB_._duplicated_files.csv'
# duplicate_files_map = pickle.load(open('12TB_._duplicated_files.pkl', 'rb'))
# count = 0
# with open(duplicated_files_keys_csv, 'r', encoding="utf-8") as f_duplicated_files_keys_csv:
#     with open(duplicated_files_values_csv, 'w', encoding="utf-8") as f_duplicated_files_values_csv:
#         line = f_duplicated_files_keys_csv.readline()
#         while line:
#             count += 1
#             print(str(count))
#             key = line.rstrip()
#             value = duplicate_files_map[key]
#             f_duplicated_files_values_csv.write(str(value))
#             f_duplicated_files_values_csv.write("\n")
#             del key
#             del value
#             if count % 1000 == 0:
#                 f_duplicated_files_values_csv.flush()
#                 f_duplicated_files_keys_csv.flush()
#                 print("flush " + str(count))
#             del line
#             line = f_duplicated_files_keys_csv.readline()


duplicated_files_csv = '12TB_._duplicated_files2.csv'
duplicate_files_map = pickle.load(open('12TB_._duplicated_files2.pkl', 'rb'))
count = 0
with open(duplicated_files_csv, 'w', encoding="utf-8") as f_duplicated_files_csv:
    for key, value in duplicate_files_map.items():
        count += 1
        line = str(count) + "," + key + ", \"" + str(value) + "\"\n"
        f_duplicated_files_csv.write(line)
        del key
        del value
        if count % 1000 == 0:
            f_duplicated_files_csv.flush()
            print("flush " + str(count))
    # f_duplicated_files_csv.write(json.dumps(duplicate_files_map))

# duplicate_files_map = pickle.load(open('12TB_._duplicated_files2.pkl', 'rb'))
# for key, value in duplicate_files_map.items():
#     if len(value) > 1:
#         print(key, ' ', str(value))

# input_dir_path = 'test'
# duplicated_files_map = dict()
# for i in range(100000000):
#     duplicated_files_map[str(i)] = str(i)
#
# duplicated_files_csv = os.path.basename(input_dir_path) + '_duplicated_files.pkl'
# pickle.dump(duplicated_files_map, open(duplicated_files_csv, 'wb'))

# duplicate_files_map = pickle.load(open(duplicated_files_csv, 'rb'))
# for key, value in duplicate_files_map.items():
#     print(key, ' ', str(value))

# files_hashes_map = FileHashHelper.get_folder_files_hashes('D:\\MyDocuments')
# for key, value in files_hashes_map.items():
#     if len(value) > 1:
#         print(key, ' ', value)

# D:\MyDocuments

# print(FileHashHelper.get_file_hash("main.py"))
# i = 0
# for elem in Path('D:\\MyDocuments').rglob('*'):
#     if os.path.isfile(elem):
#         i = i + 1
#         print(elem, FileHashHelper.get_file_hash(elem))
#
# print(i)

# print(FileHashHelper.get_folder_files_hashes('D:\\MyDocuments'))
