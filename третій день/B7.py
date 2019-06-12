ALPHA = "".join(map(chr, range(ord(" "), ord("¤") + 1)))
 
def encode(text, step):
    return text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))
 

b = input("Введіть значення зсуву: ")


a = input("Повідомлення яке хочете зашифрувати: ")

print(encode(a, int(b)))



import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)
