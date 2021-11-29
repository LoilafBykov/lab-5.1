import os
import csv
new_file="number.txt"
line=("-----------------------------------------------")
while True:
    print(line)
    print("[1] - Зчитування файлу\n[2] - Запис у файл")
    print(line)
    what=int(input("Оберіть операцію:"))
    if what==1:
        fd=open(new_file, "r")
        read_code=csv.reader(fd, delimiter="\t")
        for series in read_code:
            print(series)
        fd.close()
        print('Операція "Зчитування файлу" пройшла успішно!')
    elif what==2:
        fd = open(new_file, "w")
        for i in range(7):
            A = i*35
            fd.write("%i\t%.1f\n" % (i, A))
        fd.close()
        print('Операція "Запис у файл" пройшла успішно')
    else:
        print("Операція хибна! Спробуйте ще раз")
input()