from pymodbus.client import ModbusTcpClient


import socket
# Crear un socket del lado del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Definir la dirección IP y el puerto del servidor
host = '127.0.0.1'
port = 502
# Conectar al servidor
client_socket.connect((host, port))
# Recibir datos del servidor
data = client_socket.recv(1024)
print("Mensaje recibido del servidor:", data.decode())
# Cerrar el socket del cliente
client_socket.close()