import socket
HOST = "127.0.0.1"
PORT = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST,PORT))
    s.listen(1)
    conn, addr = s.accept() #bloqueante
    print (f"Conexión OK con el cliente. IP {addr[0]} Puerto {addr[1]}")
    conn.close()
except socket.error as exc:
    print ("Excepción de socket: %s" % exc)
finally:
    s.close()