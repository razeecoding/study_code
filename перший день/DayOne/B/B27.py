for i in range (0,128):
    b = chr(i)
    r = ord(b)
    c = bin(i)
    t = hex(i)
    f = oct(i)
    print( b, "   ", r, "   ", c, "   ", t, "   ", f)

import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")