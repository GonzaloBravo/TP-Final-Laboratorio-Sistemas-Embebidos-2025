# Codigo para ejecutar en la Raspberry Pi

import RPi.GPIO as GPIO
import socket
import time

# Configuración de la Raspberry Pi
GPIO.setmode(GPIO.BOARD)

# Pines de los botones y LEDs
botones = {11: 7, 13: 15, 15: 29}  # {botón: LED}
mesas = {11: 1, 13: 2, 15: 3}  # {botón: número de mesa}

# Configurar botones como entrada con pull-up y LEDs como salida
for boton, led in botones.items():
    GPIO.setup(boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)  # Asegurar que los LEDs inician apagados

# Configuración del socket UDP
DIRECCION_IP = "192.XXX.X.XXX"  # IP de la PC principal
PUERTO = 5000
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Función para enviar mensaje a la PC y encender LED
def presionar_boton(channel):
    mesa = mesas[channel]
    led = botones[channel]

    # Enviar mensaje a la PC
    mensaje = f"Llamado Mesa {mesa}"
    udp_socket.sendto(mensaje.encode(), (DIRECCION_IP, PUERTO))
    print(f"Mensaje enviado: {mensaje}")

    # Encender LED por 2 segundos
    GPIO.output(led, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(led, GPIO.LOW)

# Configuracion de los botones
for boton in botones.keys():
    GPIO.add_event_detect(boton, GPIO.FALLING, callback=presionar_boton, bouncetime=300)

# Mantener el programa corriendo
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nSaliendo...")
    GPIO.cleanup()
    udp_socket.close()
