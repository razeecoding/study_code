import datetime

start = float(input("Грошей покладено на рахунок:"))
y1 = start + (start * 0.14)
y2 = y1 + (y1 * 0.14)
y3 = y2 + (y2 * 0.14)
print("1 рiк:", float('{:.2f}'.format(y1)))
print("2 рiк:", float('{:.2f}'.format(y2)))
print("3 рiк:", float('{:.2f}'.format(y3)))

def printTimeStamp(name):
    print('Автори програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")