import ui

def readFormat1():
    f1 = open('phoneBook.csv', 'r')
    lst = f1.readline()
    phoneBook = []
    while len(lst) > 0:
        record = lst.split(';')
        phoneBook.append(record)
        lst = f1.readline()

    return phoneBook

def saveFormat1(phoneBook):
    f2 = open('phoneBook.csv', 'w')
    for record in range(len(phoneBook)):
        for item in range(len(phoneBook[record])):
            f2.write(str(phoneBook[record][item]))
            if item != len(phoneBook[record])-1:
                f2.write(';')
        if record != len(phoneBook)-1:
            f2.write('\n')
    f2.close()