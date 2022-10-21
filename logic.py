import ui
import file

def mainProgram():
###### Главная программа ######
    phoneBook = []
    while True:
        choice = ui.mainMenu()
        if choice == 1:
            # Из какого формата читать ?
            format = ui.getFormat()
            # Прочитать файл выбранного формата
            if format == 1:
                phoneBook = file.readCsv()
            if format == 2:
                phoneBook = file.readTxt()

        elif choice == 2:
            # Вывести записи справочника на экран
            ui.printPhoneBook(phoneBook)

        elif choice == 3:
            # Добавить запись
            ui.addRecord(phoneBook)

        elif choice == 4:
            # Удалить запись
            ui.deleteRecord(phoneBook) 

        elif choice == 5:
            # Редактировать запись
            ui.editRecord(phoneBook) 

        elif choice == 6:
            # Спросить в какой формат сохранить
            format = ui.getFormat()
            # Сохранить файл
            if format == 1:
                file.saveCsv(phoneBook)
            if format == 2:
                file.saveTxt(phoneBook)
        
        elif choice == 0:
            break
        input("Press Enter to continue...")

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