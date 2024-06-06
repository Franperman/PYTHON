import socket

# Crear un socket del lado del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la dirección IP y el puerto para escuchar conexiones
host = '127.0.0.1'
port = 502

# Vincular el socket a la dirección IP y el puerto
server_socket.bind((host, port))

# Escuchar hasta 1 conexión entrante
server_socket.listen(1)
print("Esperando conexiones entrantes...")

while True:
    # Aceptar una conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f"Conexión aceptada desde: {client_address}")

    # Enviar el mensaje al cliente
    message = f"Tengo poca esperanza de vida. Debería estar muerto"
    client_socket.send(message.encode())

    # Cerrar la conexión con el cliente
    client_socket.close()
