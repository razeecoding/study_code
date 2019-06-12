
import random

n = 1000
def dice(n):
    for i in range(1, n + 1):
        p = random.randint(1, 6) + random.randint(1, 6)
        i += 1
        yield p

l = []
for i in dice(n):
    l.append(i)
print("{:8}{:8}".format("Total", "Simulated percent"))
for i in range(2,13):
    print("{:2}{:15}".format(i, l.count(i)/10))
    i = i + 1

import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)