

def precedence(a):
    if a =="+"or a == "-":
        return 1
    elif a =="/"or a == "*":
        return 2
    elif a=="^":
        return 3
    else:
        return -1,"Не введено оператора"
while True:
    if __name__ == "__main__":
        print(precedence(input("Введіть знак: ")))


import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)