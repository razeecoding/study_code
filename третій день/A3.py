def expt(b, n):
    if n==0:
        return 1
    return b*expt(b, n-1)


import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)