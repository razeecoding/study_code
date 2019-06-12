import datetime

ibs = input("ISBN: ")
numb = list(ibs)
s = int(numb[0]) + int(numb[1])*3 + int(numb[2]) + int(numb[3])*3 + int(numb[4]) + int(numb[5])*3 + int(numb[6]) + int(numb[7])*3 + int(numb[8]) + int(numb[9])*3 + int(numb[10]) + int(numb[11])*3
n = 10 -(s % 10)
print("The check digit:", n)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")