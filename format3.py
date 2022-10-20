# Формат файла "phoneBook.format3":
# Фамилия1;Имя1;Телефон1;Описание1
# Фамилия2;Имя2;Телефон2;Описание2

import re


def read():
    # читает файл с именем "phoneBook.format3", 
    # возращает список списков вида (("фамилия1", "имя1", "телефон1", "описание1"), ("фамилия2", "имя2", "телефон2", "описание2")...)
    return phoneBook

def save(phoneBook):
    # Сохраняет переданный список вида (("фамилия1", "имя1", "телефон1", "описание1"), ("фамилия2", "имя2", "телефон2", "описание2")...)
    # в файл с именем "phoneBook.format3"
    # ничего не возвращает

    f2 = open('phoneBook.format3', 'w')
    for record in range(len(phoneBook)):
        for item in range(len(phoneBook[record])):
            f2.write(phoneBook[record][item])
            if item != len(phoneBook[record])-1:
                f2.write(';')
        if record != len(phoneBook)-1:
            f2.write('\n')
    f2.close()
    