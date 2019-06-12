a = int(input('Введіть число:'))
b = 0
lis = []
for i in range(2,a+1):
    lis.append(i)
for z in lis:
    p = lis[b]
    b += 1
    if z**2 >= a:
        break
    for i in lis:
        if i % p == 0 and i != p:
            lis.remove(i)
print(lis)


import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)