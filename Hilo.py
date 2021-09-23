import threading, time

HORA = '11:27:00'

def contar():
    Alarma = ''
    while Alarma!=HORA:
        currentTime=time.ctime()
        currentTime=currentTime.split()   #['Tue', 'Oct', '29', '12:38:44', '2019']
        Alarma=currentTime[3]
        print('aun no es la hora, la hora actual es ', Alarma)
    print('La hora ',Alarma,' es igual a la hora programada ',HORA)
        

hilo1 = threading.Thread(target=contar)
hilo1.start()

