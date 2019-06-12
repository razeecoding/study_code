prompt = "Введіть число: "
sum = 0
count = 1
while True:
    s = input(prompt)
    prompt = "Введіть інше число : "
    if s.lower() == '':
        break
    try:
        sum += float(s)
        print ("Ви ввели %s чисел сума яких %s." % (count, sum))
        count += 1
    except ValueError:
        print( "Неправильний  ввід")
print ("Ви ввели %s чисел сума яких %s." % (count, sum))
import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)
