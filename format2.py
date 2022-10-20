import ui

def readFormat2():
    f1 = open('phoneBook.txt', 'r')
    lst = f1.readline()
    phoneBook = []
    while len(lst) > 0:
        record = lst.split(';')
        phoneBook.append(record)
        lst = f1.readline()

    return phoneBook

def saveFormat2(phoneBook):
    f2 = open('phoneBook.txt', 'w')
    for record in range(len(phoneBook)):
        for item in range(len(phoneBook[record])):
            f2.write(str(phoneBook[record][item]))
            if item != len(phoneBook[record])-1:
                f2.write(';')
        if record != len(phoneBook)-1:
            f2.write('\n')
    f2.write('\n')
    f2.close()