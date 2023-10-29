from network import *
import usocket as socket

SSID='Arduino Nano AP DE Irving'
#PASSWORD='12345678'
ap_if = WLAN(AP_IF)
ap_if.active(True)
ap_if.config(ssid=SSID)
ip=ap_if.ifconfig()[0]
print('Access Point en la dirección',ip)

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
        <body bgcolor=#FFC9DE>
            <h1>Servidor Micropython Arduino Nano RP2040 de Irving</h1>
        </body>
    </html>
    """
    client_socket.sendall(response.encode())
    client_socket.close()
