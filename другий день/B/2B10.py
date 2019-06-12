i = 0
a = input("Введіть IPv4: ")
if a.count(".")!=4:
    i+=5
b = a.split(".")
del(b[-1])
for x in b:
    try:
        if 0<=int(x)<=225:
            i+=1
    except:
        i+=5
if i ==4:
     print("Bірний ІР")
else:
    print("Невірний ІР")


import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)