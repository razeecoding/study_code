import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)

pres1 = [".","A","a","D","d","G","g","J","j","M","m","P","p","T","t","W","w"]
pres2 = [",","B","b","E","e","H","h","K","k","N","n","Q","q","U","u","X","x"]
pres3 = ["?","C","c","F","f","I","i","L","l","O","o","R","r","V","v","Y","y"]
pres4 = ["!",None,None,None,None,None,None,None,None,"S","s",None,None,"Z","z"]
pres5 = [":"]
total = [pres1, pres2, pres3, pres4, pres5]
while True:
    a = list(input("Ваш текст :"))
    s = ""
    for i in a:
        if i == " ":
            s += "0"
        for x in total:
            try:
                s+=(str(((x.index(x)+1)//2)+1)*(total.index(x)+1))
            except:
                pass
    print(s)

