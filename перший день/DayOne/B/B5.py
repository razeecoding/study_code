from math import floor
import datetime

def printTimeStamp(name):

	print('Автор програми: ' + name)

	print('Час компіляції: ' + str(datetime.datetime.now()))

	printTimeStamp("Diakov and Zanko")

def main():
    while True:
        a = int(input("Введіть сумму: "))
        b = floor(a)

        if b > 0:
            break

    
    g5 = b // 500
    g2 = (b % 500) // 200
    g1 = ((b % 500) % 200) // 100
    k50 = (((b % 500) % 200) % 100) // 50
    k25 = ((((b % 500) % 200) % 100) % 50) // 25

    print(g5,g2,g1,k50,k25)


if __name__ == "__main__":
    main()