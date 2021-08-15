import RPi.GPIO as GPIO
import time
from time import sleep
# Inicializamos el uso de la identificacion BCM para los GPIO
GPIO.setmode(GPIO.BCM)

M_In1 = 15
M_In2 = 14
M_Enable = 18

GPIO.setup(M_In1,GPIO.OUT)
GPIO.setup(M_In2,GPIO.OUT)
GPIO.setup(M_Enable,GPIO.OUT)

# Creamos la instancia PWM con el GPIO a utilizar y la frecuencia de la señal PWM
p = GPIO.PWM(M_Enable, 50)
#Inicializamos el objeto PWM
p.start(0)

vel=int(input("Velocidad del motor 0 - 101: "))

print("Hacemos girar el motor en un sentido por 10 segundos mientras aumentamos  y disminuimos la velocidad")
# Establecemos el sentido de giro con los pines IN1 e IN2  
GPIO.output(M_In1,GPIO.HIGH)
GPIO.output(M_In2,GPIO.LOW)  

#Aumenta velocidad
for m in range(0, vel, 1):
    p.ChangeDutyCycle(m)
    time.sleep(0.05)

time.sleep(10)

#Disminuye velocidad
for m in range(vel, -1, -1):
    p.ChangeDutyCycle(m)
    time.sleep(0.05)

print ("Detenemos el motor")
p.ChangeDutyCycle(0)
sleep(1)

GPIO.cleanup()
