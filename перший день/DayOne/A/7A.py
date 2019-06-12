import datetime

chel = float(input("Людськi роки:"))
if 0 < chel <= 2:
    pes = 10.5 / chel
    print("Собачi роки:", pes)
elif chel > 2:
    pes = 10.5 + (chel * 4)
    print("Собачi роки:", pes)
elif chel < 0:
    print("Введено вiд'ємне число")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")