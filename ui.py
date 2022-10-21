import os
import logic
import logger

def getFormat():
    isBadChoise = False
    while True:
        os.system('cls')
        if isBadChoise:
            print('!!!', 'Не допустимое значение - ' + str(choice), "!!!")
            isBadChoise = False
        print("Допустимые форматы:")
        print("1. CSV")
        print("2. TXT")
        choice = input("Выберете формат:")
        isBadChoise = logic.checkBadChoise(choice, 1, 2)
        if not isBadChoise:
            return int(choice)


def mainMenu():
    isBadChoise = False
    while True:
        os.system('cls')
        if isBadChoise:
            print('!!!', 'Не допустимое значение - ' + str(choice), "!!!")
            isBadChoise = False
        print("1. Прочитать справочник")
        print("2. Вывести записи справочника на экран")
        print("3. Добавить запись")
        print("4. Удалить запись")
        print("5. Редактировать запись")
        print("6. Сохранить справочник")
        print("0. Выход")
        choice = input("Выберете действие:")
        isBadChoise = logic.checkBadChoise(choice, 0, 6)
        if not isBadChoise:
            return int(choice)


def printPhoneBook(book):
    header = ['Familia    ', 'Imja       ', 'Telefon    ', 'Description']

    if(len(book) > 0):
        for i in range(len(book)):
            print('-'*40)
            print(' '*10, '№', i+1)
            for j in range(len(book[0])):
                print(header[j], ':', book[i][j])
            print('-'*40)
    else:
        print('Справочник пуст.')


def addRecord (book):
    record = []
    surname = input('Введите фамилию: ')
    record.append(surname)
    name = input('Введите имя: ')
    record.append(name)
    phone_number = getPhone()
    record.append(phone_number)
    comment = input('Введите комментарий: ')
    record.append(comment)
    print('\nКонтакт успешно добавлен\n')
    book.append(record)
    logger.number_logger(f'Добавили контакт: {surname}')
    return book

def getPhone():
    valid =False
    while not valid:      
        try:
            phone_number = input('Введите номер телефона, начиная с 8: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    return phone_number

def deleteRecord(book):
    print('Удаление контакта')
    required = getRecordNumber(book)
    delF = book[required][0] 
    del book[required]
    print('\nКонтакт успешно удалён!\n')
    logger.number_logger(f'Удалили контакт: {delF}')


def getRecordNumber(book):
    while True:
        text = f'Введите порядковый номер контакта из диапазона [1 : {len(book)}]: '
        num = input(text)
        isBadChoise = logic.checkBadChoise(num, 1, len(book))
        if not isBadChoise:
            break
        print('Неверное значение, проверте корректность ввода')
    return int(num)-1


def editRecord(book):
    print('Редактирование контакта')
    recordForEdit = getRecordNumber(book)
    print(f'Текущая фамилия: {book[recordForEdit][0]}. Введите новую фамилию или нажмите Enter, чтобы оставить без именений')
    newSurname = input()
    print(f'Текущее имя: {book[recordForEdit][1]}. Введите новое имя или нажмите Enter, чтобы оставить без именений')
    newName = input()
    print(f'Текущий номер: {book[recordForEdit][2]}. Введите новый номер или нажмите Enter, чтобы оставить без именений')
    newPhone = str(getPhone())
    print(f'Текущий комментарий: {book[recordForEdit][3]}. Введите новый комментарий или нажмите Enter, чтобы оставить без именений')
    newComment = input()

    if len(newSurname) > 0:
        oldSurname = book[recordForEdit][0]
        book[recordForEdit][0] = newSurname
        logger.number_logger(f'Изменена фамилия контакта с {oldSurname} на {newSurname}')
    if len(newName) > 0:
        oldName = book[recordForEdit][1]
        book[recordForEdit][1] = newName
        logger.number_logger(f'Изменено имя контакта с {oldName} на {newName}')
    if len(newPhone) > 0:
        oldPhone = book[recordForEdit][2]
        book[recordForEdit][2] = newPhone
        logger.number_logger(f'Изменен номер телефона контакта с {oldPhone} на {newPhone}')
    if len(newComment) > 0:
        oldComment = book[recordForEdit][3]
        book[recordForEdit][3] = newComment
        logger.number_logger(f'Изменен комментарий контакта с {oldComment} на {newComment}')