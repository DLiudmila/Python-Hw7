import ui

def readFormat2():
    file = 'phoneBook.txt'
    return open(file).read().split('\n')

def saveFormat2():
    file = 'phoneBook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {book[record][0]}\n\nИмя: {book[record][1]}\n\nНомер телефона: {book[record][2]}\n\nОписание: {book[record][3]}\n\n\n')