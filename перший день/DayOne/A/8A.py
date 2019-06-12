import datetime

shtuchku = float(input("Скільки штучок ви хочете придбати? "))
shtukencii = float(input("Скільки штукенцій ви хочете придбати?"))

mass =(shtuchku * 75)+(shtukencii * 112)
print("Вага замовлення дорінює = " + str(mass),"грам")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')