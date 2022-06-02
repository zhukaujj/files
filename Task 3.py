import os
from pprint import pprint

BASE_PATH = os.getcwd()
log_path = 'files_task_3'

files_path = os.path.join(BASE_PATH, log_path)
list_files = os.listdir(files_path)


def merge(path):
    list_file = os.listdir(path)
    dict_file = {}

    for file in list_file:
        file_to_open = os.path.join(files_path, file)
        with open(file_to_open, encoding='utf-8') as file_obj:
            files = len(file_obj.readlines())
            file_obj.seek(0)
            data_file = file_obj.read()
            dict_file[files] = {'name': file, 'data': data_file}
    sorted_file_tuple = dict(sorted(dict_file.items()))

    with open('text.txt', 'w', encoding='utf-8') as file:
        for k, v in sorted_file_tuple.items():
            res = v['name'] + '\n' + str(k) + '\n' + v['data']
            file.write(res + '\n')
    pprint(sorted_file_tuple)

merge(files_path)

