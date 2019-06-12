print("Місце проживання (Гуртожиток, Квартира, Будинок)")
home = input('Введіть місце проживання: ')

time = int(input('Введіть скільки годин ви приблизно знаходитесь дома: '))
print('                                           ')

if home =='Гуртожиток':
	
	if time < 6:
	  print('Тобі підійде: Мурашник')
	
elif time == 6 :
      print('Тобі підійде: Мурашник або рибки')
     
if time > 6:
	  print('Тобі підійдуть: Рибки')

if home =='Квартира':
	
  if time <10 :
     print("Тобі підійде: Хом'як")



if home =='Квартира' and time == 10 :
	print("Тобі підійде: Хом'як або Кішка")


if home =='Квартира' and time > 10:
	print('Тобі підійде: Кішка')


if home =='Будинок' and time <=10 :
	print("Тобі підійде: Змія")	


if home =='Будинок' and time >10 and time <17:
	print("Тобі підійде: Собака")


if home =='Будинок' and time > 18:
	print('Тобі підійде: В’єтнамське порося')

import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')
