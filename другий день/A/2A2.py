

l = []
lless = []
lmore = []

while True:
    n = input("Bведiть число: ")
    if n == '':
        break
    else:
        n = float(n)
        l.append(n)

avg = sum(l) / len(l)
for i in range(len(l)):
    if l[i] < avg:
        lless.append(l[i])
    elif l[i] >= avg:
        lmore.append(l[i])
    else:
        print('')
print("Не перевищують за середнє значення: ", lless)
print("Бiльше або рiвнi за середнє значення: ", lmore)


import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)