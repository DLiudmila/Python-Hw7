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
        print("1. format1")
        print("2. format2")
        print("3. format3")
        print("4. format4")
        choice = input("Выберете формат:")
        isBadChoise = logic.checkBadChoise(choice, 1, 4)
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
    #TODO: Доделать
    header = ['Familia    ', 'Imja       ', 'Telefon    ', 'Description']

    for i in range(len(book)):
        print('-'*40)
        print(' '*10, '№', i+1)
        for j in range(len(book[0])):
            print(header[j], ':', book[i][j])
        print('-'*40)


def addRecord (book):
    record = []
    surname = input('Введите фамилию: ')
    record.append(surname)
    name = input('Введите имя: ')
    record.append(name)
    phone_number = ''
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
    record.append(phone_number)
    comment = input('Введите комментарий: ')
    record.append(comment)
    print('\nКонтакт успешно добавлен\n')
    book.append(record)
    logger.number_logger(f"Добавили контакт: {surname}")
    return book


def deleteRecord(book):
    print("Удаление контакта")
    required = getRecordNumber(book)
    delF = book[required-1][0] 
    del book[required-1]
    print('\nКонтакт успешно удалён!\n')
    logger.number_logger(f"Удалили контакт: {delF}")


def getRecordNumber(book):
    while True:
        text = f"Введите порядковый номер контакта из диапазона [1 : {len(book)}]: "
        num = input(text)
        isBadChoise = logic.checkBadChoise(num, 1, len(book))
        if not isBadChoise:
            break
        print("Неверное значение, проверте корректность ввода")
    return int(num)


def editRecord(book, recordNum):
    print("Редактирование контакта")
    required = getRecordNumber(book)
    print('Введите')
