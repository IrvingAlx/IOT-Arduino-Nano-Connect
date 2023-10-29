from machine import Pin, PWM
import usocket as socket
from network import *
from time import *

#RGB
Red = 0
Green = 1
Blue = 2

# Declare pins
pwm_pins = [25,15,16]
# Setup pins for PWM
pwms = [PWM(Pin(pwm_pins[Red])),PWM(Pin(pwm_pins[Green])),
                PWM(Pin(pwm_pins[Blue]))]

[pwm.freq(1000) for pwm in pwms]

def set_rgb_color(color):
    if color == "Pink":
        pwms[Red].duty_u16(65535)  
        pwms[Green].duty_u16(0)
        pwms[Blue].duty_u16(65535)
        print("Hola rosa")
    elif color == "Yellow":
        pwms[Red].duty_u16(65535)
        pwms[Green].duty_u16(65535)
        pwms[Blue].duty_u16(0)
    elif color == "Skyblue":
        pwms[Red].duty_u16(0)
        pwms[Green].duty_u16(65535)
        pwms[Blue].duty_u16(65535)
    elif color == "Orange":
        pwms[Red].duty_u16(65535)
        pwms[Green].duty_u16(32767)
        pwms[Blue].duty_u16(0)
    elif color == "White":
        pwms[Red].duty_u16(65535)
        pwms[Green].duty_u16(65535)
        pwms[Blue].duty_u16(65535)
    elif color == "Red":
        pwms[Red].duty_u16(65535)
        pwms[Green].duty_u16(0)
        pwms[Blue].duty_u16(0)
    elif color == "Green":
        pwms[Red].duty_u16(0)
        pwms[Green].duty_u16(65535)
        pwms[Blue].duty_u16(0)
    elif color == "Blue":
        pwms[Red].duty_u16(0)
        pwms[Green].duty_u16(0)
        pwms[Blue].duty_u16(65535)
    else:
        pwms[Red].duty_u16(0)
        pwms[Green].duty_u16(0)
        pwms[Blue].duty_u16(0)

sta_if=WLAN(STA_IF)
sta_if.active(True)
print('Activando estación...')
while not sta_if.active():
    pass
print('Estación activada!...')
sta_if.connect('Guapo quien lo lea','1029384756')
print('Conectando...')
while not sta_if.isconnected():
    pass
print('Conectado!')
print("IP:",sta_if.ifconfig()[0])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8080))  
server_socket.listen(10)

print("Esperando conexiones...")

while True:
    client_socket, client_address = server_socket.accept()
    print("Conexión establecida desde:", client_address)

    data = client_socket.recv(1024)
    print("Datos recibidos:", data.decode())
    
    if b'Pink=on' in data:
        set_rgb_color("Pink")
        print("Hola")
    if b'Yellow=on' in data:
        set_rgb_color("Yellow")
    if b'Skyblue=on' in data:
        set_rgb_color("Skyblue")
    if b'Orange=on' in data:
        set_rgb_color("Orange")
    if b'White=on' in data:
        set_rgb_color("White")
    if b'led=off' in data:
        set_rgb_color("Off")
    if b'Red=on' in data:
        set_rgb_color("Red")
    if b'Green=on' in data:
        set_rgb_color("Green")
    if b'Blue=on' in data:
        set_rgb_color("Blue")

    response = """HTTP/1.1 200 OK
    Content-Type: text/html

    <html>
        <head><title>Servidor MicroPython</title></head>
        <body bgcolor=#9BD0B7>
            <h1>Servidor Micropython Arduino Nano de Irving</h1>
        </body>
    </html>
    """
    client_socket.sendall(response.encode())
    client_socket.close()