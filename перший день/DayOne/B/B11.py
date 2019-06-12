import math
import datetime

shir = math.radians(50)
dovg = math.radians(36.15)
shir2 = math.radians(50.27)
dovg2 = math.radians(30.30)
shir3 = math.radians(46.28)
dovg3 = math.radians(30.43)

vidst1 = 6371.01 * math.acos(math.sin(shir) * math.sin(shir2) + math.cos(shir) * math.cos(shir2) * math.cos(dovg - dovg2))
vidst2 = 6371.01 * math.acos(math.sin(shir2) * math.sin(shir3) + math.cos(shir2) * math.cos(shir3) * math.cos(dovg2 - dovg3))
vidst3 = 6371.01 * math.acos(math.sin(shir) * math.sin(shir3) + math.cos(shir) * math.cos(shir3) * math.cos(dovg - dovg3))

p = (vidst1 + vidst2 + vidst3) / 2
s = math.sqrt(p * (p - vidst1) * (p - vidst2) * (p - vidst3))

print(" Вiдстань вiд Харкова до Києва:", vidst1, "км", "\n", "Вiдстань вiд Одеси до Києва:", vidst2, "км", "\n", "Вiдстань вiд Харкова до Одеси:", vidst3, "км", "\n", "Площа трикутника:", s, "кв.км")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")