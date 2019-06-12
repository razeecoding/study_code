import datetime

def printTimeStamp(name):

	print('Автори програми: ' + name)

	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Diakov and Zanko")
	
mark = input('Введіть буквенну оцінку(від A до F): ')

if mark == 'A+' :
	print('Оцінка більше 4 балів')
elif mark == 'A' :
	print('Ваша оцінка становить: 4.0 бала')
elif mark == 'A-' :
	print('Ваша оцінка становить: 3.7 бала')
elif mark == 'B+' :
	print('Ваша оцінка становить: 3.3 бала')
elif mark == 'B' :
	print('Ваша оцінка становить: 3.0 бала')
elif mark == 'B-' :
	print('Ваша оцінка становить: 2.7 бала')
elif mark == 'C+' :
	print('Ваша оцінка становить: 2.3 бала')
elif mark == 'C' :
	print('Ваша оцінка становить: 2.0 бала')
elif mark == 'C-' :
	print('Ваша оцінка становить: 1.7 бала')
elif mark == 'D+' :
	print('Ваша оцінка становить: 1.3 бала')
elif mark == 'D' :
	print('Ваша оцінка становить: 1.0 бал')
elif mark == 'F' :
	print('Ваша оцінка становить: 0 балiв')
else:
	print('Помилка, введіть буквенну оцінку від A до F')