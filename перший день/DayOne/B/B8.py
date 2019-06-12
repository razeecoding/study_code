import datetime

path = input("Введіть номерний знак: ")
bukwy = path[0:3]
cifry = path[3:7]
cifry2 = path[0:4]
bukwy2 = path[4:7]
old_bukwy = bukwy.isupper()
old_cifry = cifry.isdigit()
new_cifry = cifry2.isdigit()
new_bukwy = bukwy2.isupper()

if old_bukwy == True and old_cifry == True:
	print("Старий номерний знак")
elif new_cifry == True and new_bukwy == True:
	print("Новий номерний знак")
else:
	print("Номер неправильний")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")