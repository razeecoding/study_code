import datetime

m = int(input("Яка масса води: "))
T = int(input("Температура: "))
C = 4.186
q = (m/1000)*T*C
print(q)

def printTimeStamp(name):

	print('Автори програми: ' + name)

	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Diakov and Zanko")