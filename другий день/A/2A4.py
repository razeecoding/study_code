﻿
import random

article = ['the', 'a', 'one', 'some', 'any']
noun = ['boy', 'girl', 'dog', 'town', 'car']
verb = ['drove', 'jumped', 'ran', 'walked', 'skipped']
preposition = ['to', 'from', 'over', 'under', 'on']

for i in range(10):
    print('{} {} {} {} {} {}.'.format(
    article[random.randint(0,4)].capitalize(),
    noun[random.randint(0,4)],
    verb[random.randint(0,4)],
    preposition[random.randint(0,4)],
    article[random.randint(0,4)],
    noun[random.randint(0,4)]))

import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)