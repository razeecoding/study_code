x = int(input("Enter the x part of the coordinate: "))
y = int(input("Enter the y part of the coordinate: "))
z = []
while True:
    x1 = int(input("Enter the x part of the coordinate: (blank to quit): "))
    y1 = int(input("Enter the y part of the coordinate: "))
    z.append(x1)
    z.append(y1)
    if x1 == " ":
   		break
       
z.pop()


import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")