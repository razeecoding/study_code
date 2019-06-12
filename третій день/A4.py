def MinusPower(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return x**n
    elif n % 2 == 0:
        return MinusPower(x, n/2)**2
    else:
        return x * MinusPower(x, n-1)

print(MinusPower(2,-1))

import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)