from ui import addRecord
info = addRecord

def readFormat1():
        file = 'phoneBook.csv'
        return open(file).read().split('\n')

def saveFormat1():
    file = 'phoneBook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}, Имя: {info[1]}, Номер телефона: {info[2]}, Описание: {info[3]}\n')