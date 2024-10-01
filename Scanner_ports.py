import socket

ip = input("ingrese la direccion ip a escanerar: ")

for puerto in range(1,655356):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    result = sock.connect_ex((ip, puerto))

    if  result == 0:
        print("Puerto Abierto: " + str(puerto))
        sock.close()
    else:
        print("Puerto Cerrado: " + str(puerto))