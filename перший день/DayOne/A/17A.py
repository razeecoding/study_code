import datetime
import math

s = int(input("Довжина сторони:"))
n = int(input("Кiлькiсть сторiн:"))
pl = ((n * (s**2)) / (4 * math.tan(math.pi / n)))
print("Площа полiгону:", float('{:.5f}'.format(pl)))

def printTimeStamp(name):
    print('Автори програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")