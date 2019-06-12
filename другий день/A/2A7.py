
import pprint

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

pprint.pprint(l)


import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)