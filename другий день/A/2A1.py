import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)

l = []

while True:
    n = input("Введiть число(Для сортування введiть пустий рядок):")
    if n == '' and len(l) >= 6:
        l.sort()
        for i in range(3):
            l.pop(0)
            l.pop()
        print(l)
    elif n.isdigit():
        l.append(int(n))
    elif len(l) < 6:
        print("Мало чисел")
    else:
        print("Помилка")