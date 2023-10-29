from network import *
from time import *
import usocket as socket
from machine import *

led = Pin(25,Pin.OUT)
led2 = Pin(15,Pin.OUT)
led3 = Pin(16,Pin.OUT)
led4 = Pin(17,Pin.OUT)

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

    if b'led=on' in data:
        led.on()
    if b'led=off' in data:
        led.off()
    if b'led2=on' in data:
        led2.on()
    if b'led2=off' in data:
        led2.off()
    if b'led3=on' in data:
        led3.on()
    if b'led3=off' in data:
        led3.off()
    if b'led4=on' in data:
        led4.on()
    if b'led4=off' in data:
        led4.off()
    if b'led5=on' in data:
        while (True):
            led.on ()
            sleep (0.1)
            led.off ()
            sleep (0.1)
            led2.on ()
            sleep (0.1)
            led2.off ()
            sleep (0.1)
            led3.on ()
            sleep (0.1)
            led3.off ()
            sleep (0.1)
            led4.on ()
            sleep (0.1)
            led4.off ()
            sleep (0.1)    

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