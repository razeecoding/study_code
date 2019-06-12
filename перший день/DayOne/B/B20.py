import datetime

def printTimeStamp(name):

	print('Автори програми: ' + name)

	print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp("Diakov and Zanko")

a = 0
b = 0
while True:
    mark = float(input("Введіть оцінку: "))
    a += 1
    b += mark
    if mark > 4:
        print("Оцінка: А+")
    elif 3.7 <   mark <= 4:
        print("Оцінка : А")
    elif 3.3 < mark <= 3.7:
        print("Оцінка : A-")
    elif 3.0 < mark <= 3.3:
        print("Оцінка : B+")
    elif 2.7 < mark <= 3:
        print("Оцінка : B")
    elif 2.3 < mark <= 2.7:
        print("Оцінка : B-")
    elif 2 < mark <= 2.3:
        print("Оцінка : C+")
    elif 1.7 < mark <= 2:
        print("Оцінка : C")
    elif 1.3 < mark <= 1.7:
        print("Оцінка : C-")
    elif 1 < mark <= 1.3:
        print("Оцінка : D+")
    elif 0 < mark  <= 1:
        print("Оцінка : D")
    elif mark == 0:
        print("Оцінка : F")
    elif mark == -1:
        a -= 1
        b -= mark
        break
    else:
        a -= 1
        b -= mark
        print("Такої оцінки немає")
c =(b/a)*10
if c in range(0,9):
	print("Буквений варіант: F")
elif c in range(10, 12):
	print("Буквений варіант: D")
elif c in range(13, 16):
	print("Буквений варіант: D+")
elif c in range(17, 19):
	print("Буквений варіант: C-")
elif c in range(20, 22):
	print("Буквений варіант: C")
elif c in range(23, 26):
	print("Буквений варіант: C+")
elif c in range(27, 29):
	print("Буквений варіант: B-")
elif c in range(30, 32):
	print("Буквений варіант: B")
elif c in range(33, 36):
	print("Буквений варіант: B+")
elif c in range(37, 39):
	print("Буквений варіант: A-")
elif c == 40:
	print("Буквений варіант: A")
elif c > 40:
	print("Буквений варіант: A+")

print("Середня оцінка: ")
d = c/10
print(d)