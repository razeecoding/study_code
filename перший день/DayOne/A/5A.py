temperature = float(input("Введіть температуру в Цельсіях = "))

temp_Kelvin =(temperature + 273)
print("Цельсії в Кельвінах =" + str(temp_Kelvin))
temp_Farengate =(temperature*1.8 + 32)
print("Цельсії в Фарингейтах =" + str(temp_Farengate))

import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')