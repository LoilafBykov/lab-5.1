import os
import csv
import random
import filecmp
def read_file(file): 
    fd=open(file,'r')
    read_code=csv.reader(fd, delimiter='\t')
    for series in read_code:
        print(series)
    fd.close()
    print('Операія "Зчитування файлу" успішна!')
def write_file(file):
    fd=open(file,'w')
    for i in range(5):
        A=i*38
        fd.write('%i\t%.1f\n'%(i,A))
    fd.close()
    print('Операція "Запис файлу" успішна!')
def new_name(file):
    os.new_name('D:\\Рабочий стол\\number2.txt','D:\\Рабочий стол\\number.txt')
    print('Операція "Перейменування файлу" успішна!')
def sorting(file):
    for file in os.listdir('D:\Рабочий стол\\lab-5.1'):
        print(file)
    print('Операція "Перебір файлів у каталозі" успішна!')
def comparis(file):
    alike=filecmp.cmp('D:\\Рабочий стол\\number2.txt','D:\\Рабочий стол\\number.txt')
    print(alike)
    print('Операція "Порівняння файлів" успішна!')
def app_file(file):
    fd=open(file,'a')
    for i in range(7):
        A=random.randint(25,42)
        fd.write_file('%i\t%.1f\n'%(i,A))
    fd.close()
    print('Операція "Дозапис у кінець файлу" успішна!')


file='number2.txt'
line=("-----------------------------------------------")
while True:
    print('[1] - Зчитування файлу\n[2] - Запис файлу\n[3] - Дозапис у кінець файлу\n[4] - Перейменування файлу\n[5] - Перебір файлів у каталозі\n[6] - Порівняння файлів')
    choice=int(input('Оберіть операцію:'))
    if choice==1:
        read_file(file)
        print(line)
    elif choice==2:
        write_file(file)
        print(line)
    elif choice==3:
        app_file(file)
        print(line)
    elif choice==4:
        new_name(file)
        print(line)
    elif choice==5:
        sorting(file)
        print(line)
    elif choice==6:
        comparis(file)
        print(line)
    else:
        print('Хибна операція')
        print(line)
input()