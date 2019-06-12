import datetime

n = int(input("Перше число: "))
m = int(input("Друге число: "))
while n != 0 and m != 0:
    if n > m:
        n %= m
    else:
        m %= n
print(n+m)

def printTimeStamp(name):

	print('Автори програми: ' + name)

	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Diakov and Zanko")
