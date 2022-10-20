import ui
import format1
import format2

def mainProgram():
###### Главная программа ######
    phoneBook = [['Sidorov', 'Sidr', '111-22-33', 'Opisanie Sidorova']]
    while True:
        choice = ui.mainMenu()
        if choice == 1:
            # Из какого формата читать ?
            format = ui.getFormat()
            # Прочитать файл выбранного формата
            if format == 1:
                phoneBook = format1.readFormat1()
            if format == 2:
                phoneBook = format2.readFormat2()


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
            # Запросить номер записи для редактирования
            recordNumber = ui.getRecordNumber(phoneBook)
            # Редактировать запись
            ui.editRecord(phoneBook, recordNumber) 

        elif choice == 6:
            # Спросить в какой формат сохранить
            format = ui.getFormat()
            # Сохранить файл
            if format == 1:
                format1.saveFormat1(phoneBook)
            if format == 2:
                format2.saveFormat2(phoneBook)
        
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