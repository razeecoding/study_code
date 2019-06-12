num_1 = int(input("Num 1 : "))
num_2 = int(input("Num 2 : "))
num_3 = int(input("Num 3 : "))
num_list = []
num_list.append(num_1)
num_list.append(num_2)
num_list.append(num_3)
num_list.sort()
maxi = max(num_list)
mini = min(num_list)
print(num_list)
print("Max num: " + str(maxi) , " Min num: " + str(mini))

import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')
