﻿

prov = {'A':'Newfoundland',
        'B':'Nova Scotia',
        'C':'Prince Edward Island',
        'E':'New Brunswick',
        'G':'Quebec',
        'H':'Quebec',
        'J':'Quebec',
        'K':'Ontario',
        'L':'Ontario',
        'M':'Ontario',
        'N':'Ontario',
        'P':'Ontario',
        'R':'Manitoba',
        'S':'Saskatchewan',
        'T':'Alberta',
        'V':'British Columbia',
        'X':'Nunavut або Nortwest Territories',
        'Y':'Yukon'}
while True:
    try:
        code = list(input('Введіть код: '))
        code[1] = int(code[1])
        code[3] = int(code[3])
        code[5] = int(code[5])
    except ValueError:
        print('Некоректний код')
        continue
    if len(code) == 6:
        break
    else:
        print('Некоректний код')
        continue
for i in prov:
    if i == code[0]:
        print(prov.get(i))
    else:
        continue
if code[1] == 0:
    print('Село')
else:
    print('Місто')


import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)