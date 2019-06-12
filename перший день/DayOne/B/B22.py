import datetime

chast = int(input("Частота:"))


if 0 < chast < 3 * (10**9):
    print("Radio waves")
elif 3 * (10**9) <= chast < 3 * (10**12):
    print("Microwaves")
elif 3 *(10**10) <= chast < 4.3 * (10**14):
    print("Infrared light")
elif 4.3 * (10**14) <= chast < 7.5 * (10**14):
    print("Visible light")
elif 7.5 * (10**14) <= chast < 3 * (10**17):
    print("Ultraviolet light")
elif 3 * (10**17) <= chast < 3 * (10**19):
    print("X-rays")
elif chast >= 3 * (10**19):
    print("Gamma rays")
else:
    print("Частоту введено неправильно!")

def printTimeStamp(name):

	print('Автори програми: ' + name)

	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Diakov and Zanko")