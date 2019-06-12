pressure_kpa = float(input("Введіть тиск у КПа: "))
psi = pressure_kpa * 0.15
mm = pressure_kpa *  7.5
atmo = pressure_kpa *  0.01
print("Фунти на кв.дюйм: " , str(psi)  )
print("мм ртутного стовчика: " , str(mm))
print("Атмосфери: " , str(atmo))

import datetime 
def printTimeStamp(name):                    
	print('Автор програми: ' + name)                
	print('Час компіляції: ' + str(datetime.datetime.now()))    
printTimeStamp('Diakov and Zanko')