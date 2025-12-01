import socket

HOST = ''  # todas las tarjetas o interfaces
PORT = 2000

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()  # línea bloqueante

        with conn:
            print(f"Conexión con éxito desde IP: {addr[0]} Puerto: {addr[1]}")
            while True:
                data = conn.recv(1024)  # línea bloqueante
                print(data)
                if data == b"0":
                    break
                conn.sendall(b"mensaje recibido")

except ConnectionRefusedError:
    print("Error: no se pudo conectar al servidor.")

except socket.timeout:
    print("Error: la operación excedió el tiempo de espera.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
