import datetime

def printTimeStamp(name):

	print('Автор програми: ' + name)

	print('Час компіляції: ' + str(datetime.datetime.now()))

	printTimeStamp("Diakov ans Zanko")

xv = int(input("Скільки ви використали хвилин: "))
sms = int(input("Скільки смс ви використали: "))
a = 35
b = (a*0.05) + 0.44 + a

if xv>200:
	a += (xv-200)*0.17

if sms>50:
	a += (sms - 50)*0.17

print("Рахунок без податків: " + str('{:.2f}'.format(b)))
print("Загальний рахунок: " + str('{:.2f}'.format(b)))