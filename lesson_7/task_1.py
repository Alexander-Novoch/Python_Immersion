# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
from os import path
import shutil

type_sort = ['text', 'video', 'image', 'other']


def sort_files(type: list) -> None:
    os.chdir("testdir")  # дирректория была создана из кода семинара
    for i in range(len(type)):
        if not path.exists(type[i]):
            os.mkdir(f'{type[i]}')

    folder_track = os.getcwd()
    folder_move = os.getcwd()

    files = os.listdir(folder_track)
    for items in files:
        extension = items.split(".")
        if len(extension) > 1 and (
                extension[1].lower() == "jpg" or
                extension[1].lower() == "png" or
                extension[1].lower() == "svg"):
            file = folder_track + "\\" + items
            new_path = folder_move + "\\image\\" + items
            shutil.move(file, new_path)
        elif len(extension) > 1 and (extension[1].lower() == 'avi' or
                                     extension[1].lower() == 'mpg' or
                                     extension[1].lower() == 'gif' or
                                     extension[1].lower() == 'mp4' or
                                     extension[1].lower() == 'mpeg' or
                                     extension[1].lower() == 'mpg' or
                                     extension[1].lower() == 'flac'):
            file = folder_track + "\\" + items
            new_path = folder_move + "\\video\\" + items
            shutil.move(file, new_path)
        elif len(extension) > 1 and (extension[1].lower() == 'txt' or
                                     extension[1].lower() == 'doc' or
                                     extension[1].lower() == 'docx' or
                                     extension[1].lower() == 'rtf'):
            file = folder_track + "\\" + items
            new_path = folder_move + "text" + items
            shutil.move(file, new_path)
        else:
            file = folder_track + "\\" + items
            new_path = folder_move + "\\other\\" + items
            shutil.move(file, new_path)


# def get_file_paths(folder_path) -> list:
#     file_paths = [f.path for f in os.scandir(os.getcwd()) if not f.is_dir()]
#     return file_paths


if __name__ == '__main__':
    sort_files(type_sort)
