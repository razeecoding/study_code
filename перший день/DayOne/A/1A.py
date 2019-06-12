imt_method = str(input("Дюйми/Футы(1) , Метри/Кілограми(2)"))

if imt_method == "1":
	weight = float(input("Введіть масу: "))
	height = float(input("Введіть зріст: "))
	imt1 = (703 * weight) / (height ** 2)
	print("IMT: " + str(imt1) )

if imt_method == "2":
	weight = float(input("Введіть масу: "))
	height = float(input("Введіть зріст: "))
	imt2 = weight / (height ** 2)
	print("IMT: " + str(imt2) )

import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')