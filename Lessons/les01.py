#utf 8

import os

print("Project les01 started")
print("privet")


name = input("Ваше имя: ")
print(name, "псина")

answer = input("Го работать? (Y/N)" )
if answer.lower() == 'y':
    print("Шо ты хочиш ат миня?9(((99((")
    print("1 - Вывести список файлов в текущей директории")
    print("2 - Вывести информацию о системе")
    #print("3 - Поработать дома")
    do = int(input("Укажи номер действия: "))

    if do == 1:
        print(os.listdir())
    elif do == 2:
        pass
    else:
        pass


elif answer.lower() == 'n':
        print("Ой, всё(((")
else:
    print("Че ты пишешь?")
