f = open(r'A8.txt' , 'r')
openf = f.read()
print(openf)
f = open(r'A8.txt' , 'r')
splitf = f.read().split('\n')
strlist = ''.join(splitf)
f = open(r'A8.txt' , 'w')
splitready = f.write(strlist)
f = open(r'A8.txt' , 'r')
ready = f.read()
print(ready)
