import math
import datetime

shir = math.radians(float(input("Широта 1 точки:")))
dovg = math.radians(float(input("Довгота 1 точки:")))
shir2 = math.radians(float(input("Широта 2 точки:")))
dovg2 = math.radians(float(input("Довгота 2 точки:")))
vidst = 6371.01 * math.acos(math.sin(shir) * math.sin(shir2) + math.cos(shir) * math.cos(shir2) * math.cos(dovg - dovg2))
print("Вiдстань:", vidst, "км")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")