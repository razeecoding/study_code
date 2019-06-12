import datetime

a = str(input("Позначки:"))
if a == "Вiдпустка" or "вiдпустка":
    print("Будильник вимкнено")
elif a == "Вихiдний" or "вихiдний":
    print("Будильник вимкнено")
else:
    print("Будильник ввiмкнено")


def printTimeStamp(name):
    print('Автори програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")