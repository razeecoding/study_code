import random, datetime

point = 0
trys = 1
while trys == 1:
    trys -= 1
    kubiki= [random.randint(1,6) for i in range(6)]
    print(kubiki)
    point += kubiki.count(1) * 100
    point += kubiki.count(5) * 50
    break_group = 0
    for i in range (1,7):
        if kubiki.count(i) >=3:
            print("{} однакові кості '{}' +{}".format(kubiki.count(i), i, (kubiki.count(i)- 2) * 100 *(10 if i == 1 else i)))
            point += (kubiki.count(i)-2) * 100 *(10 if i == 1 else 1)
            break_group += 1
    if len(set(kubiki)) == 3 and break_group == 0:
        print("Три пари, +750 points та ще одна спроба")
        point += 750
        trys += 1
    if len(set(kubiki)) == 6:
        print("Три пари, +1500 points та ще одна спроба")
        point += 1500
        trys +=1
print("Ваші points", point)

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')