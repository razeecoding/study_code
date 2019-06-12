num = input('Введіть 4-х значне число: ')

num_list = list(num)

num_1 = int(num_list[0])
num_2 = int(num_list[1])
num_3 = int(num_list[2])
num_4 = int(num_list[3])

print(num_1 + num_2 + num_3 + num_4)

import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')

