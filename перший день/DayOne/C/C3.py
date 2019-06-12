side_temperature= int(input("Введіть температуру на вулиці: "))
room_temperature= int(input("Введіть температуру в кімнаті: "))
time=0
kof=0
termo=True
while time!= 24:
    if  5<=time<=15:
        side_temperature+=1
    else:
        side_temperature-=1
    if 22<=room_temperature<=24 and termo==True:
        termo= False
        kof=0
        for i in range(8):
            print("Температура в кімнаті - {:.2f}`C. Година - {}:00. Термостат працює.".format(room_temperature,time if time> 9 else "0"+str(chasiki)))
            room_temperature= room_temperature+k*(room_temperature-side_temperature)
            if 5 <= time <= 15:
                side_temperature += 1
            else:
                side_temperature -= 1
            time+=1
    elif 22<=room_temperature<=24 and termo==False:
        kof=-0.02
        room_temperature = room_temperature + kof * (room_temperature - side_temperature)
        time+=1
        print("Температура в кімнаті - {:.2f}`C. Година - {}:00. Всі прилади вимкнені.".format(room_temperature,time if time > 9 else "0" + str(time)))

    elif room_temperature<22:
        kof=0.11
        room_temperature = room_temperature + kof * (room_temperature - side_temperature)
        time+=1
        print("Температура в кімнаті - {:.2f}`C. Година - {}:00. Обігрівач працює.".format(room_temperature,time if time > 9 else "0" + str(time)))

    elif room_temperature>24:
        kof=-0.09
        room_temperature = room_temperature + kof * (room_temperature - side_temperature)
        time+=1
        print("Температура в кімнаті - {:.2f}`C. Година - {}:00. Кондіціонер працює.".format(room_temperature,time if time > 9 else "0" + str(time)))
        time+=1
    elif room_temperature < 0:
        print("Invalid Input")


import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Diakov and Zanko')




