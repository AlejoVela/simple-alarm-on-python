from Alarm import Alarm


ListAlarm = []

print('Cuantas alarmas desea ingresar?')
num=int(input())


for i in range(num):

    print('Ingrese la hora de la alarma')
    hour = input()
    print('Ingrese los minutos')
    minutes = input()
    print('Ingrese los segundos') 
    second = input()

    time = f'{hour}:{minutes}:{second}'

    print('la hora programada para la alarma es ',time)
    ListAlarm.append(Alarm(time))


for i in range(num):
    ListAlarm[i].iniciar()
    
    


#x = Alarm('15:36:00')
#x1= Alarm('15:01:30')