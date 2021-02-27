import sys 
from math import ceil

#Задание 1

hashSize = 255
hashTabl = [None for i in range(hashSize)]

string = input("Введите строку \n")
stringSet = set(string)

for i in stringSet:
    hashIndex = ord(i)%hashSize #Хеш-функция: ascii код символа
    hashTabl[hashIndex] = (i, string.count(i))
print(hashTabl)

char =  input("Введите символ для поиска \n")
try:
    hashIndex = ord(char)%hashSize
except TypeError:
    print("Введена строка")
    sys.exit()
print(hashTabl[hashIndex])