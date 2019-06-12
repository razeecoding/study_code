import datetime

def printTimeStamp(name):

	print('Автор програми: ' + name)

	print('Час компіляції: ' + str(datetime.datetime.now()))

	printTimeStamp("Diakov and Zanko")
	
result = ''
q = int(input("число: ")) 
while q > 0:
	r = q % 2
	result = str(r) + result
	q = q // 2
print(result, "\nІніціалізувати змінну result порожнім рядком\nОголосити змінну q – число для перетворення\nrepeat\n    Оголосити r та присвоїти йому значення остачі від ділення q на 2\n    Звести r до рядкового типу та додати її до початку  result Поділити націло q на 2 та зберегти результат у q\nuntil q не доівнює 0")
