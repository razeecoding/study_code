print("Введіть рахунок за їжу:")
a = float(input())
x = a * 0.14
y = a * 0.18
z = x + y + a
print("Чайові:{:.2f}".format(x))
print("Податок:{:.2f}".format(y))
print("Разом:{:.2f}".format(z))

import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')
