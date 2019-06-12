lenght = float(input("Введіть свій зріст в сантиметрах :"))

duim = (lenght/2.54)
futt = (duim/12)

print("Ваш зріст у дюймах = " + str(duim), ", футах = " + str(futt))

import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')