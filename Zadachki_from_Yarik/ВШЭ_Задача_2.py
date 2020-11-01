import csv

# Функции для консоли
#


def CallHistory(b):
    loop = True
    count = 0
    while loop == True:
        print("Enter the target phone number: ")
        mun = str(input())
        for phone in b:
            if phone['recipent'] == mun or phone['sender'] == mun:
                loop = False
            else:
                count += 1
            if len(b) == count:
                print("Phone number not find in the database")
                continue
    print("Call history with " + mun + ":")

    name = num + "_" + mun + ".txt"
    with open(name, "w") as tfile:
        for phone in book:
            if phone['sender'] == num and phone['recipent'] == mun:
                if int(phone['sec']) >= 0:
                    print("In: " + phone['date'] + " " + phone['time'] + " - " + str(
                        int(phone['sec'])//60) + " min " + str(int(phone['sec']) % 60) + " sec")
                    tfile.write("In: " + phone['date'] + " " + phone['time'] + " - " + str(
                        int(phone['sec'])//60) + " min " + str(int(phone['sec']) % 60) + " sec")
                else:
                    print("In: " + phone['date'] + " " +
                          phone['time'] + " - missed")
                    tfile.write(
                        "In: " + phone['date'] + " " + phone['time'] + " - missed")
            if phone['recipent'] == num and phone['sender'] == mun:
                if int(phone['sec']) >= 0:
                    print("Out: " + phone['date'] + " " + phone['time'] + " - " + str(
                        int(phone['sec'])//60) + " min " + str(int(phone['sec']) % 60) + " sec")
                    tfile.write("Out: " + phone['date'] + " " + phone['time'] + " - " + str(
                        int(phone['sec'])//60) + " min " + str(int(phone['sec']) % 60) + " sec")
                else:
                    print("Out: " + phone['date'] +
                          " " + phone['time'] + " - rejected")
                    tfile.write(
                        "Out: " + phone['date'] + " " + phone['time'] + " - rejected")
    print("Call history saved in file " + num + "_" + mun + ".txt")

#


def CallStatics(b):
    billforOut = 0
    averageOut = 0
    billforIn = 0
    averageIn = 0
    missed = 0
    rejected = 0
    for phone in b:
        if phone['sender'] == num:
            if int(phone['sec']) >= 0:
                billforOut += 1
                averageOut = int(phone['sec'])
            else:
                rejected += 1
        if phone['recipent'] == num:
            if int(phone['sec']) >= 0:
                billforIn += 1
                averageIn = int(phone['sec'])
            else:
                missed += 1
    if billforOut > 0:
        print(str(billforOut) + " accepted outgoing call(s), average time: " +
              str((averageOut//billforOut)//60) + " min " + str((averageOut//billforOut) % 60) + " sec")
    else:
        print("No accepted outgoing call(s) were found")
    if billforIn > 0:
        print(str(billforIn) + " accepted incoming call(s), average time: " +
              str((averageIn//billforIn)//60) + " min " + str((averageIn//billforIn) % 60) + " sec")
    else:
        print("No accepted outgoing call(s) were found")
    print(str(missed) + " missed call(s)")
    print(str(rejected) + " rejected call(s)")


# Тело основной программы
# Ввод из csv файла
book = []
with open('Desktop\example.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    count = 0
    for row in reader:
        book.append({'sender': row[0], 'recipent': row[1],
                     'date': row[2], 'time': row[3], 'sec': row[4]})

# Запрос номера
loop = True
count = 0
while loop == True:
    print("Enter your phone number: ")
    num = str(input())
    for phone in book:
        if phone['sender'] == num:
            loop = False
        else:
            count += 1
        if len(book) == count:
            print("Phone number not find")
            continue

# Алгоритм
loop = True
while loop == True:
    print("Select an action:" + "\n" + "1 - Call statics" + "\n" +
          "2 - Call history with other contact" + "\n" + "3 - Exit" + "\n" + "Your choice: ")
    answer = int(input())
    if answer == 1:
        CallStatics(book)
        print("\n")
    if answer == 2:
        CallHistory(book)
        print("\n")
    if answer == 3:
        loop = False
