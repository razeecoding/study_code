import re
text_string = 'Some index files failed To download, they have been ignored, or ones used instead.459'
low = []
high = []
num = []
for i in text_string:
    if i.islower():
        low.append(i)
    elif i.isupper():
        high.append(i)
print("Words: {}\nSpaces: {}\nLow: {}\nHigh: {}\nNums: {}\nLeters: {}".format(len(text_string.split(' ')), (text_string.count(" ")), len(low), len(high), len(re.findall(r'\d', text_string)), len(low)+len(high)))


import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)