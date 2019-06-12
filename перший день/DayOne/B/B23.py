import datetime
voda = float(input("Споживання води:"))

if voda <= 30:
    a = 20 + (voda * 9.86)
    print("Ваш рахунок:", a, "грн")
elif 30 < voda <= 50:
    b = 20 + (30 * 9.86) + ((voda - 30) * 11.22)
    print("Ваш рахунок:", b, "грн")
elif 50 < voda <= 60:
    c = 20 + (30 * 9.86) + (20 * 11.22) + ((voda - 50) * 13.06)
    print("Ваш рахунок:", c, "грн")
elif voda > 60:
    d = 20 + (30 * 9.86) + (20 * 11.22) + (10 * 13.06) + ((voda - 60) * 17.89)
    print("Ваш рахунок:", d, "грн")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")