rf = open("teht.txt")
wf = open("newteht.txt","w")
for string in rf:
    new_string = string.replace("\n","")
    wf.write(new_string)
    wf.write('. ')
rf.close()
wf.close()


import datetime

def printTimeStamp(name):

  print('Автор: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
name="Diakov and Zanko"
printTimeStamp(name)