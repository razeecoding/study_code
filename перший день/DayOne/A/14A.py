import datetime

a = int(input("Скільки вчорашных буханок ви хочете купити: "))
b = a * 8.5
c = (a * 8.5)*0.4
d = b - c
print("Звичайна ціна: " + str(b) + " Ваша снижка: " + str(d) + " Загальна ціна: " + str('{:.2f}'.format(c)))

def printTimeStamp(name):

	print('Автори програми: ' + name)

	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Diakov and Zanko")