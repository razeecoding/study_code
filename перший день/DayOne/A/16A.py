import datetime
import math

r = int(input("Введiть радiус:"))
krug = math.pi * (r**2)
kulya = 4/3 * math.pi * (r**3)
print("Площа кругу:", float('{:.5f}'.format(krug)), "\n", "Об'єм кулi:", float('{:.5f}'.format(kulya)))

def printTimeStamp(name):
    print('Автори програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")