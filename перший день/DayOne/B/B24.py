import datetime

db = int(input("Noise lvl(dB):"))
if db > 130:
    print("More than Jackhammer")
elif db == 130:
    print("Jackhammer")
elif 106 < db < 130:
    print("Between Jackhammer and Gas lawnmower")
elif db == 106:
    print("Gas lawnmower")
elif 70 < db < 106:
    print("Between Gas lawnmower and Alarm clock")
elif db == 70:
    print("Alarm clock")
elif 40 < db < 70:
    print("Between Alarm clock and Quiet room")
elif db == 40:
    print("Quiet room")
elif db < 40:
    print("Lower than Quiet room")

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Diakov and Zanko")