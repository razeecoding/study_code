import random


l = []

mast = ['s', 'h', 'd', 'c']
val = ['J', 'Q', 'K', 'A']

for i in range(len(mast)):
    for n in range(2, 11):
        c = str(n) + str(mast[i])
        l.append(c)
    for v in range(len(val)):
        c = str(val[v]) + str(mast[i])
        l.append(c)

def Sattolo(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = random.randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]
    print("Перетасована колода:", items)

print("Колода:", l)

Sattolo(list(l))

import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)