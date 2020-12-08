# utf 8   flake8 Q:\GitHub\Python\Lessons
# lesson 3 - type, dir, help, pip, import + os, sys, psutil
# import psutil, dir(psutil) = список команд
import os  # Подключение модуля
import sys
import psutil  # Подключение стороннего модуля
import shutil


def duplicate_file(filename):
    if os.path.isfile(filename):
        new_file = filename + '.dupl'
        shutil.copy(filename, new_file)
        if os.path.exists(new_file):
            print("Файл", new_file, "успешно скопирован.")
            return True
        else:
            print("Возникли проблемы с копированием")
            return False
    else:
        print("Ошибка: %s файл не найден" % copy_directory)

def sys_info():
    print("Имя ОС:", os.name)
    print("Процессор содержит", psutil.cpu_count(), "ядер")
    print("Кодировка файловой системы:", sys.getfilesystemencoding())
    print("Логин пользователя:", os.getlogin())

def delete_dupl_files(directory):
    delete_files = os.listdir(directory)
    deleted_files_counter = 0

    for file in delete_files:
        if file.endswith('.dupl'):
            os.remove(file)
            if not os.path.exists(file):
                deleted_files_counter += 1
                print("Файл", file, "был успешно удалён")

    return deleted_files_counter


print("Project les01 started")
print("privet")

os.chdir(path=r"E:\GitHub\Python\Lessons")
name = input("Ваше имя: ")
print(name, " - псина")

answer = ''
while answer.lower() != 'q':
    answer = input("Го работать? (Y/N/Q)")
    if answer.lower() == 'y':
        print("Шо ты хочиш ат миня?9(((99((")
        print("1 - Вывести список файлов в текущей директории")
        print("2 - Вывести информацию о системе")
        print("3 - Вывести список процессов")
        print("4 - Продублировать файлы в текущей директории")
        print("5 - Продублировать заданный файл в заданной директории")
        print("6 - Удалить файлы '.dupl' в заданной директории")
        do = int(input("Укажи номер действия: "))

        if do == 1:
            print("В директории ", os.getcwd(), " содержатся файлы: ",
                  os.listdir(path=r"Q:\GitHub\Python\Lessons"))
        elif do == 2:
            sys_info()
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("=Дублирование файлов в текущей директории", os.getcwd(),
                    '\n')
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                duplicate_file(file_list[i])
                i += 1
        elif do == 5:
            print("=Дублирование заданного файла в заданной директории=", '\n')
            copy_directory = input("Укажите директорию с именем файла: \n")
            #  file_list = os.listdir()
            #  path="Q:\GitHub\Python\Lessons"
            duplicate_file(copy_directory)

        elif do == 6:
            print("=Удалить файлы '.dupl' в заданной директории=", '\n')
            directory = input("Задайте директорию: \n")
            print(delete_dupl_files(directory))

        else:
            pass
    elif answer.lower() == 'n':
        print("Ой, всё(((")
    elif answer.lower() == 'q':
        break
    else:
        print("Че ты пишешь?")
