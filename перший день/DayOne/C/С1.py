import datetime, random
allplases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, "0", "00"]
reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
blacks = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def oneNumber(num):
    win = random.choice(allCell)
    if (win == "0" or win == "00") and num == win:
        return win
    else:
        print("На рулетці випало", win)
        if win == int(num):
            print("Виплатити", win)
        else:
            print("Ви програли")

def red_black(color):
    win = random.choice(allCell)
    print("На рулетці випало", "Червоне" if win in reds else "Чорне" if win in blacks else win)
    print("Виплатити Червоне") if ((win in reds) and color == "Червоне") else print("Виплатити Чорне") if (win in blacks) and color == "Чорне" else print("Ви програли")

def parne_neparne(choice):
    win = random.randint(1, 36)
    print("На рулетці випало", win)
    if ((win % 2 == 0) and choice == "Парне"):
        print("Виплатити Парне")
    elif (win % 2 != 0) and choice == "Непарне":
        print("Виплатити Непарне")
    else:
        print("Ви програли")

def inHalf(choice):
    win = random.choice(allCell)
    print("На рулетці випало", win)
    if (win <= 18 and choice == "First"):
        print("Виплатити 1 to 18")
    elif win >= 19 and choice == "Second":
        print("Виплатити 19 to 36")
    else:
        print("Ви програли")

while True:
    betOneNumber = oneNumber(input("\n{}\nВведіть число для ставки 'Одне число' (від 1 до 36, 0 або 00): ".format("="*15)))
    if betOneNumber != None:
        print("Виплатити", betOneNumber)
        continue
    betRed_Black = red_black(input("Введіть колір для ставки 'Червоне vs Чорне' (Червоне або Чорне): "))
    betparne_neparne = parne_neparne(input("Введіть вибір для ставки 'Парне vs Непарне' (Парне або Непарне): "))
    betInHalf = inHalf(input("Введіть вибір для ставки 'Від 1 до 18 vs від 19 до 36' (First або Second): "))

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")