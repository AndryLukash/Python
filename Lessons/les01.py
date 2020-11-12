#utf 8
# lesson 3 - type, dir, help, pip, import + os, sys, psutil
import os # Подключение модуля
import sys
import psutil # Подключение стороннего модуля

print("Project les01 started")
print("privet")


name = input("Ваше имя: ")
print(name, "псина")

answer = input("Го работать? (Y/N)" )
if answer.lower() == 'y':
    print("Шо ты хочиш ат миня?9(((99((")
    print("1 - Вывести список файлов в текущей директории")
    print("2 - Вывести информацию о системе")
    # имя тек дир, ОС, кодировка файловой, логин пользоаптеля, кол-во процессоров
    print("3 - Вывести список процессов")
    do = int(input("Укажи номер действия: "))

    if do == 1:
        print("В директории ", os.getcwd(), " содержатся файлы: ", os.listdir())
    elif do == 2:
        pass
    elif do == 3:
        print(psutil.pids())
    else:
        pass

elif answer.lower() == 'n':
        print("Ой, всё(((")
else:
    print("Че ты пишешь?")
