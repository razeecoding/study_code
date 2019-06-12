import datetime

t = float(input("Температура(до 10 C):"))
v = float(input("Швидкiсть вiтру(понад 4.8 км/год):"))
if t <= 10 and v > 4.8:
    index = 13.12 + (0.6215 * t) - (11.37 * (v**0.16)) + (0.3965 * t * (v**0.16))
    print("WCL: ", round(index))
else:
    print("Некоректнi даннi")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")