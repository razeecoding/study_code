
import winsound

ar1 = [659, 659, 659, 523, 659, 784,
    392, 523,392, 330, 440, 494,
    466, 440, 392, 659, 784, 880,
    698, 784, 659, 523, 587, 494]
ar2 = [250, 250, 300, 250, 250, 300,
    300, 275, 275,275, 250, 250,
    275, 275, 275, 250, 250, 275,
    275, 225, 250, 250, 225, 225]
for i in range(len(ar2)):
    winsound.Beep(ar1[i], ar2[i])


import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)