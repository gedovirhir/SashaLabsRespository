import sys 
from math import ceil

#Задание 3
f = open("data1.txt", "r")
words = f.readlines()
words = [i.rstrip().split(" ") for i in words]
words = words[0]
f.close()

m = len(words)
hashSize = ceil(m*1.5) #Будем использовать квадратичное опробывание для решения коллизий => делаем размер таблицы в 1.5 больше количества элементов
hashTabl = [-1 for i in range(hashSize)]

for i in words:
    index = 0 #Переменнная, используемая для решения коллизий
    hashIndex = int(i) % 100 % hashSize #Хеш-функция: остаток от деления на 100

    while (hashTabl[(hashIndex + index**2) % hashSize] != -1) and (index < m):
        index += 1
    if index > m: 
        print("Переполнение таблицы")
        sys.exit()
    hashTabl[(hashIndex + index**2) % hashSize] = int(i)
print("Хеш-таблица: ")
print(hashTabl)

num = int(input("Введите число для поиска \n"))

index = 0
hashIndex = num %100 %hashSize
while (hashTabl[(hashIndex + index**2) % hashSize] != num) and (hashTabl[(hashIndex + index**2) % hashSize] != -1):
    index += 1
if hashTabl[(hashIndex + index**2) % hashSize] == -1:
    print("Данного числа нет в таблице")
else:    print("Индекс введенного числа: " + str((hashIndex + index**2) % hashSize))