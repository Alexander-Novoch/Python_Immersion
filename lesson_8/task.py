# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер \
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import os
import json
import csv
import pickle


def directory_to_files_recurs(path_directory: str) -> None:
    dir_dict = {}

    for dir_path, dir_name, file_name in os.walk(path_directory):
        new_dir_name = []
        new_file_name = []
        if dir_name:
            for i in range(len(dir_name)):
                new_dir_name.append(f' - {get_size(dir_name[i])} byte')
        elif file_name:
            for j in range(len(file_name)):
                new_file_name.append(f' - {get_size_file(file_name[j])} byte')

        dir_dict[dir_path] = [f'directory - {dir_name + new_dir_name}', f'files - {file_name + new_file_name}']

    with open('Sem_8.json', 'w', encoding='utf-8') as json_file:
        json.dump(dir_dict, json_file, indent=2, ensure_ascii=False)
    # print(dir_dict)

    # with open('Sem8.csv', 'w', encoding='utf-8', newline='') as csv_file:
    #     csv_dict = csv.DictWriter(csv_file, fieldnames=['Path', 'Content'], dialect='excel-tab')
    #     csv_dict.writeheader()
    #     csv_dict.writerows(dir_dict)

    with open('Sem_8.json', 'r', encoding='utf_8') as json_file_reed:
        data = json.load(json_file_reed)
    rows = []
    for key, value in data.items():
        rows.append({'Path': key, 'Content': value})
    with open('Sem8.csv', 'w', encoding='utf-8') as csv_file:
        csv_dict = csv.DictWriter(csv_file, fieldnames=['Path', 'Content'], dialect='excel-tab')
        csv_dict.writeheader()
        csv_dict.writerows(rows)

    with open('Sem_8.pickle', 'wb') as pickle_file:
        pickle.dump(dir_dict, pickle_file)


def get_size_file(name) -> int:
    weight = os.path.getsize(str(name))
    return weight


def get_size(start_path: str):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


if __name__ == '__main__':
    print(get_size('.'), 'byte')
    directory_to_files_recurs('C:\\Users\\Xander\\Desktop\\Обучение\\Immersion in Python\\Homework\\lesson_8')
