import threading, time
from playsound import playsound

class Alarm:

    timeToSing = ''
    hilo1 = None

    def __init__(self, timeToSing):
        self.timeToSing = timeToSing
        self.hilo1 = threading.Thread(target=self.contar)
        #hilo1.start()


    def contar(self):
        Alarma = ''
        while Alarma!=self.timeToSing:
            currentTime=time.ctime()
            currentTime=currentTime.split()   #['Tue', 'Oct', '29', '12:38:44', '2019']
            Alarma=currentTime[3]
            #print('aun no es la hora, la hora actual es ', Alarma)
            time.sleep(1)   # Delays for 1 seconds. You can also use a float value.
        #print('La hora ',Alarma,' es igual a la hora programada ',self.timeToSing)
        NOMBRE_ARCHIVO = "audio.wav"
        playsound(NOMBRE_ARCHIVO)
        

    def iniciar(self):
        self.hilo1.start()

    
