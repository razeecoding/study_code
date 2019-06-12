tar = input("Введіть назву тарифу( 1000 , 2000 , 5000 ) ")


#1000mb
if tar == "1000":
	mb_status = float(input("Введіть кількість викорастаних МБ: "))
	if mb_status < 0:
		print("Input Error")
	elif mb_status <= 1000:
		print("Ваш рахунок: 20 ГРН ")
	elif mb_status > 1000:
		out_tar = (mb_status - 1000) * 0.05
		all_cost = 20 + out_tar
		print("Ваш рахунок: " + str(all_cost) + " ГРН"  )
	print("Тариф 2000: 2000МБ + 0.4ГРН позатарфино за 1МБ \nТариф 5000: 5000МБ + 0.2ГРН позатарфино за 1МБ")
	


#2000mb
if tar == "2000":
	mb_status = float(input("Введіть кількість викорастаних МБ: "))
	if mb_status < 0:
		print("Input Error")
	elif mb_status <= 2000:
		print("Ваш рахунок: 35 ГРН ")
	elif mb_status > 2000:
		out_tar = (mb_status - 2000) * 0.04
		all_cost = 35 + out_tar
		print("Ваш рахунок: " + str(all_cost) + " ГРН"  )
	print("Тариф 2000: 2000МБ + 0.4ГРН позатарфино за 1МБ \nТариф 5000: 5000МБ + 0.2ГРН позатарфино за 1МБ")
	


#5000mb
if tar == "5000":
	mb_status = float(input("Введіть кількість викорастаних МБ: "))
	if mb_status < 0:
		print("Input Error")
	elif mb_status <= 5000:
		print("Ваш рахунок: 85 ГРН ")
	elif mb_status > 5000:
		out_tar = (mb_status - 5000) * 0.02
		all_cost = 85 + out_tar
		print("Ваш рахунок: " + str(all_cost) + " ГРН"  )


import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')

