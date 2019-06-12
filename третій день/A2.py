def catalan(n):
    if n >= 2:
        c = ((2 * ((2*n) - 1)) / (n+1)) * catalan(n-1)
        return int(c)
    return 1
 
 
print(catalan(0))
print(catalan(1))
print(catalan(2))
print(catalan(3))
print(catalan(4))
import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)
