tries = 0
full = 0 
while True:
	a = int(input("Введіть число : "))
	if a == 0:
		print("Середнє значення:")
		print(full/tries)
		break
	else:
		full += a
		tries += 1
		continue

import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')

	
