from network import *
from time import *
import usocket as socket

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
    
    response = """HTTP/1.1 200 OK
    Content-Type: text/html

    <html>
        <head><title>Servidor MicroPython</title></head>
        <body bgcolor=#9BD0B7>
            <h1>Servidor Micropython ESP-32 de OMAR</h1>
        </body>
    </html>
    """
    client_socket.sendall(response.encode())
    client_socket.close()


