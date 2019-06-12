year = int(input("Введите любой год: "))
if (year % 400 == 0):
    vus_year = True
elif (year % 100 == 0):
    vus_year = False
elif (year % 4 == 0):
    vus_year = True
else:
    vus_year = False

month = int(input("Введіть любий місяць (1-12): "))
if month in (1, 3, 5, 7, 8, 10, 12):
    month_long = 31
elif month== 2:
    if vus_year:
        month_long = 29
    else:
        month_long = 28
else:
    month_long = 30
day = int(input("Введите любой день (1-31): "))
if day < month_long:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("Наступна дата(день) %d-%d-%d." % (year, month, day))
for year in (year,month,day,):
     if day > month_long:
        break

import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')
