import datetime

for i in range(1, 11):
    for j in range(1, 11):
        print("{:2d}".format(i * j), end=" ")
    print()

def printTimeStamp(name):

	print('Автори програми: ' + name)

	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Diakov and Zanko")
