import datetime

def printTimeStamp(name):

	print('Автор програми: ' + name)

	print('Час компіляції: ' + str(datetime.datetime.now()))

	printTimeStamp("Diakov and Zanko")

p = int(input("Введіть тиск: "))
v = int(input("Введіть об`єм: "))
t = int(input("Введіть температуру: "))
r = 8.314
k = t + 273.15

print("Молярна масса: ", (p*(v/1000))/(r*k))
