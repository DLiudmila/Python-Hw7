import ui

def readCsv():
    f1 = open('phoneBook.csv', 'r')
    lst = f1.readline()
    phoneBook = []
    while len(lst) > 0:
        record = lst.split(';')
        phoneBook.append(record)
        lst = f1.readline()

    return phoneBook

def saveCsv(phoneBook):
    f2 = open('phoneBook.csv', 'w')
    for record in range(len(phoneBook)):
        for item in range(len(phoneBook[record])):
            f2.write(str(phoneBook[record][item]).strip())
            if item != len(phoneBook[record])-1:
                f2.write(';')
        if record != len(phoneBook)-1:
            f2.write('\n')
    f2.close()

def readTxt():
    f1 = open('phoneBook.txt', 'r')
    phoneBook = []
    while True:
        record = []
        item = f1.readline()
        if len(item) > 0:
            item = item.replace('\r', '').replace('\n', '')
            record.append(item)
            for i in range(3):
                item = f1.readline()
                item = item.replace('\r', '').replace('\n', '')
                record.append(item)
            phoneBook.append(record)
            item = f1.readline()
            if len(item) == 0:
                break

    return phoneBook

def saveTxt(phoneBook):
    f2 = open('phoneBook.txt', 'w')
    for record in range(len(phoneBook)):
        for item in range(len(phoneBook[record])):
            f2.write(str(phoneBook[record][item]).strip())
            if item != len(phoneBook[record])-1:
                f2.write('\n')
        if item == len(phoneBook[record])-1 and record != len(phoneBook)-1:
            f2.write('\n\n')
    f2.close()