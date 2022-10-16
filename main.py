import os
import format1
import format2
import format3
import format4

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
        isBadChoise = checkBadChoise(choice, 1, 4)
        if not isBadChoise:
            return int(choice)


def checkBadChoise(input, min, max):
    # Проверка на не цифры
    try:
        input = int(input)
    except:
        return True
    # Проверка числового значения на попадание в диапазон
    if input < min or input > max:
        return True
    else: 
        return False

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
        isBadChoise = checkBadChoise(choice, 0, 6)
        if not isBadChoise:
            return int(choice)
    

def printPhoneBook(book):
    #TODO: Доделать
    print(book)

def addRecord(book):
    #TODO: Доделать
    book.append(input("Введите данные:"))

def deleteRecord(book):
    #TODO: Доделать
    True

def getRecordNumber():
    n = 0
    #TODO: Доделать
    return n

def editRecord(book, recordNum):
    #TODO: Доделать
    True


###### Главная программа ######
phoneBook = []
while True:
    choice = mainMenu()
    if choice == 1:
        # Из какого формата читать ?
        format = getFormat()
        # Прочитать файл выбранного формата
        if format == 1:
            phoneBook = format1.readFormat1()
        if format == 2:
            phoneBook = format2.readFormat2()
        if format == 3:
            phoneBook = format3.readFormat3()
        if format == 4:
            phoneBook = format4.readFormat4()

    elif choice == 2:
        # Вывести записи справочника на экран
        printPhoneBook(phoneBook)
        input("Press Enter to continue...")
    elif choice == 3:
        # Добавить запись
        addRecord(phoneBook)
    
    elif choice == 4:
        # Удалить запись
        deleteRecord(phoneBook) 
    
    elif choice == 5:
        # Запросить номер записи для редактирования
        recordNumber = getRecordNumber()
        # Редактировать запись
        editRecord(phoneBook, recordNumber) 
    
    elif choice == 6:
        # Спросить в какой формат сохранить
        format = getFormat()
        # Сохранить файл
        if format == 1:
            format1.saveFormat1(phoneBook)
        if format == 2:
            format2.saveFormat2(phoneBook)
        if format == 3:
            format3.saveFormat3(phoneBook)
        if format == 4:
            format4.saveFormat4(phoneBook)
    
    elif choice == 0:
        break