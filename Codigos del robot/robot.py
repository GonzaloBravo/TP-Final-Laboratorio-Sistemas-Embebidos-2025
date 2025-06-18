import RPi.GPIO as GPIO
import socket
import time
from time import sleep


# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pines de control de motores
Motor_A_Adelante = 18
Motor_A_Atras = 19
Motor_B_Adelante = 20
Motor_B_Atras = 21

# Configurar los pines como salidas
GPIO.setup(Motor_A_Adelante, GPIO.OUT)
GPIO.setup(Motor_A_Atras, GPIO.OUT)
GPIO.setup(Motor_B_Adelante, GPIO.OUT)
GPIO.setup(Motor_B_Atras, GPIO.OUT)

# Funciones de movimiento
def adelante():
    GPIO.output(Motor_A_Adelante, GPIO.HIGH)
    time.sleep(0.650)
    GPIO.output(Motor_A_Atras, GPIO.LOW)
    GPIO.output(Motor_B_Adelante, GPIO.HIGH)
    time.sleep(0.850)
    GPIO.output(Motor_B_Atras, GPIO.LOW)

def atras():
    GPIO.output(Motor_A_Atras, GPIO.HIGH)
    time.sleep(0.850)
    GPIO.output(Motor_A_Adelante, GPIO.LOW)
    GPIO.output(Motor_B_Atras, GPIO.HIGH)
    time.sleep(0.650)
    GPIO.output(Motor_B_Adelante, GPIO.LOW)


def detener():
    GPIO.output(Motor_A_Adelante, GPIO.LOW)
    GPIO.output(Motor_B_Adelante, GPIO.LOW)
    GPIO.output(Motor_A_Atras, GPIO.LOW)
    GPIO.output(Motor_B_Atras, GPIO.LOW)

def izquierda():
    GPIO.output(Motor_A_Adelante, GPIO.HIGH)
    GPIO.output(Motor_B_Adelante, GPIO.LOW)
    GPIO.output(Motor_A_Atras, GPIO.LOW)
    GPIO.output(Motor_B_Atras, GPIO.HIGH)

def derecha():
    GPIO.output(Motor_A_Adelante, GPIO.LOW)
    GPIO.output(Motor_B_Adelante, GPIO.HIGH)
    GPIO.output(Motor_A_Atras, GPIO.HIGH)
    GPIO.output(Motor_B_Atras, GPIO.LOW)

# Detener motores al iniciar
detener()

