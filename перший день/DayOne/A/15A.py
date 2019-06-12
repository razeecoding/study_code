import datetime

n = int(input("Введiть цiле число:"))
nast = n + 1
mnoj = n * nast
dil = mnoj / 2
print(dil)

def printTimeStamp(name):
    print('Автори програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")
