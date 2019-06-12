import datetime

def printTimeStamp(name):

	print('Автор програми: ' + name)

	print('Час компіляції: ' + str(datetime.datetime.now()))

	printTimeStamp("Diakov and Zanko")
	
year = int(input("Введіть рік: "))
if year % 400 == 0:
    print("Звичайний рік")
elif year % 100 == 0:
    if year % 4 != 0:
        print("Високосний рік")
    else:
        print("Звичайний рік")
