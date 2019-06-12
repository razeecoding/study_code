def gcd(x,y): 

    if (x == y): 
        return y
    
    if (x < y): 
        return gcd(x, y-x)
    if (x > y): 
        return gcd(x-y, y) 
     
x = 98
y = 56
if(gcd(x, y)): 
    print('НСД', x, 'і', y, 'є', gcd(x, y)) 
else: 
    print('Не знайдено') 
import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)