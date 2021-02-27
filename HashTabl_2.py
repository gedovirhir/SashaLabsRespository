import sys 
from math import ceil

#Задание 2

f = open("data.txt", "r")

hashSize = int(input("Введите размерность хеш-таблицы \n"))
hashTabl = [[] for i in range(hashSize)]
words = f.readlines()
words = [i.rstrip() for i in words]
for j in words:
    for i in j.split(" "):
        hashIndex = ord(i[0])%hashSize #Хеш-функция: ascii-код первой буквы слова 
        hashTabl[hashIndex].append(i) #Способ разрешения коллизий - метод цепочек
print(hashTabl)

findWord = input("Введите слово для поиска \n")
flag = True
for i in range(len(hashTabl[ord(findWord[0])%hashSize])):
    if findWord == hashTabl[ord(findWord[0])%hashSize][i]:
        print("Слово находится по индексу " + str(ord(findWord[0])%hashSize) + "," + str(i))
        flag = False
if flag: print("Слова нет в таблице \n")

char = input("Введите букву на которую начинаются слова для удаления \n")

i = 0
while i < len(hashTabl[ord(char[0])%hashSize]):
    if hashTabl[ord(char[0])%hashSize][i][0] == char:
        del hashTabl[ord(char[0])%hashSize][i]
    else:
        i += 1
print(hashTabl)
f.close()

