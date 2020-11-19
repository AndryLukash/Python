# utf 8
# lesson 3 - type, dir, help, pip, import + os, sys, psutil
# import psutil, dir(psutil) = список команд
import os  # Подключение модуля
import sys
import psutil  # Подключение стороннего модуля
import shutil

print("Project les01 started")
print("privet")

os.chdir("Q:\GitHub\Python\Lessons")
name = input("Ваше имя: ")
print(name, "псина")

answer = ''
while answer.lower() != 'q':
    answer = input("Го работать? (Y/N/Q)")
    if answer.lower() == 'y':
        print("Шо ты хочиш ат миня?9(((99((")
        print("1 - Вывести список файлов в текущей директории")
        print("2 - Вывести информацию о системе")
        print("3 - Вывести список процессов")
        print("4 - Продублировать файлы в текущей директории")
        do = int(input("Укажи номер действия: "))

        if do == 1:
            print("В директории ", os.getcwd(), " содержатся файлы: ",
                  os.listdir(path="Q:\GitHub\Python\Lessons"))
        elif do == 2:
            print("Имя ОС:", os.name)
            print("Процессор содержит", psutil.cpu_count(), "ядер")
            print("Кодировка файловой системы:", sys.getfilesystemencoding())
            print("Логин пользователя:", os.getlogin())
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("=Дублирование файлов в текущей директории=")
            file_list = os.listdir()
            #  path="Q:\GitHub\Python\Lessons"
            print(file_list)
            # i = 0
            # while i < len(file_list):
            #     new_file = file_list[i] + '.dupl'
            #     shutil.copy(file_list[i], new_file)
            #     i += 1
        else:
            pass
    elif answer.lower() == 'n':
        print("Ой, всё(((")
    elif answer.lower() == 'q':
        break
    else:
        print("Че ты пишешь?")
