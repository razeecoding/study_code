pib = input("Введите ваше ФИО: ")
f = open(r'A7.txt', 'r')
infile = f.read()
print("Изначальный текст")
print(infile)

f = open(r'A7.txt', 'a')
filewrite = f.write(pib)
print(filewrite)
print("Текст с ФИО")
f = open(r'A7.txt', 'r')
prf = f.read()
print(prf)

