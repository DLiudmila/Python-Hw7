import ui

def readCsv():
    file = open('phoneBook.csv', 'r')
    lst = file.readline()
    phoneBook = []
    while len(lst) > 0:
        record = lst.split(';')
        phoneBook.append(record)
        lst = file.readline()
    file.close()
    return phoneBook


def saveCsv(phoneBook):
    file = open('phoneBook.csv', 'w')
    for record in range(len(phoneBook)):
        for item in range(len(phoneBook[record])):
            file.write(str(phoneBook[record][item]).strip())
            if item != len(phoneBook[record])-1:
                file.write(';')
        if record != len(phoneBook)-1:
            file.write('\n')
    file.close()


def readTxt():
    file = open('phoneBook.txt', 'r')
    phoneBook = []
    while True:
        record = []
        item = file.readline()
        if len(item) > 0:
            item = item.replace('\r', '').replace('\n', '')
            record.append(item)
            for i in range(3):
                item = file.readline()
                item = item.replace('\r', '').replace('\n', '')
                record.append(item)
            phoneBook.append(record)
            item = file.readline()
            if len(item) == 0:
                break
    file.close()
    return phoneBook


def saveTxt(phoneBook):
    file = open('phoneBook.txt', 'w')
    for record in range(len(phoneBook)):
        for item in range(len(phoneBook[record])):
            file.write(str(phoneBook[record][item]).strip())
            if item != len(phoneBook[record])-1:
                file.write('\n')
        if item == len(phoneBook[record])-1 and record != len(phoneBook)-1:
            file.write('\n\n')
    file.close()