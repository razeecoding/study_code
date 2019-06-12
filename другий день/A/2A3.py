

l = []
while True:
    w = input("Введiть слово: ")
    if w == '':
        break
    else:
        l.append(w)

unik = []

for i in l:
    if i not in unik:
        unik.append(i)

print("Унiкальнi слова:", unik)


import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)