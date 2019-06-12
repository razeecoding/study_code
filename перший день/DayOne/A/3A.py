
while True:
	letter = str(input("Letter: "))

	if letter == "y":
		print("Може бути і такою і такою")
		continue

	elif letter == "a" and "e" and "i" and "o" and "u":
		print("Голосна!")
		continue

	elif letter == "":
		break

	else:
		print("Приголосна")
		continue


import datetime
def printTimeStamp(name):
  print('Автор програми: ' + name)
  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')