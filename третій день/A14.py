import random
lines = open('A14.txt').read().splitlines()
word1 = random.choice(lines)
word2 = random.choice(lines)
print("Your Password: " + (word1+word2))

import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')