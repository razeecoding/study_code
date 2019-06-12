
import winsound

ar = [[440,500], [440,500], [440,500], [349,350], [523,150],[440,500],
     [349,350], [523,150], [440,1000], [659,500], [659,500],[659,500],
     [698,350], [523,150], [415,500], [349,350], [523,150], [440,1000]]

for i in ar:
    print(i)
    winsound.Beep(i[0], i[1])


import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)