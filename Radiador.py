import RPi.GPIO as GPIO

import time
# Desactivamos mensajes de error
GPIO.setwarnings(False)
# Inicializamos el uso de la identificacion BCM para los GPIO
GPIO.setmode(GPIO.BCM)
# Indicamos que el GPIO24 es de salida de corriente
GPIO.setup(23,GPIO.OUT)
# en una variable guardamos el valor de PWM para el GPIO24
pwm_led=GPIO.PWM(23,500)
# iniciamos el led con longitud de pulso 100
pwm_led.start(0)
# bucle que se repetira hasta finalizar el programa
while(True):
    # disminuimos longitud del pulso
    pwm_led.ChangeDutyCycle(0)
    # esperamos medio segundo
    time.sleep(0.5)
    # aumentamos longitud del pulso
    pwm_led.ChangeDutyCycle(10)
    # esperamos medio segundo
    time.sleep(0.5)
    pwm_led.ChangeDutyCycle(20)
    time.sleep(0.5)
    pwm_led.ChangeDutyCycle(25)
    time.sleep(0.5)
    pwm_led.ChangeDutyCycle(50)
    time.sleep(0.5)
    pwm_led.ChangeDutyCycle(75)
    time.sleep(0.5)
    pwm_led.ChangeDutyCycle(100)
    time.sleep(0.5)
