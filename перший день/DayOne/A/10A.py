days = int(input("Введіть кількість днів: "))
hours = int(input("Введіть кількість годин: "))
minutes = int(input("Введіть кількість хвилин: "))
seconds = int(input("Введіть кількість секунд: "))
all_secs = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
print("У заданому проміжку часу " , str(all_secs) + (" секунд."))

import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')
