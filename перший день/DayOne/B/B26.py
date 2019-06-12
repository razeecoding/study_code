import datetime

def factorise(n):
    factors = []
    factor = 2
    if n < factor:
        print("Помилка")
        return 0
    else:
        while( factor * factor <= n) and (n >= 2):
            if n % factor == 0:
                factors.append(factor)
                n = n // factor
            else:
                factor = factor + 1

        factors.append(n)
        print("Фактори числа", n, ":",  factors)
 
n = int(input("Введiть число(бiльше 2) : "))

factorise(n)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")