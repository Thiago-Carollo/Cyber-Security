import string
import random

longintud = int(input("Ingrese el tamaño de la contraseña: "))

caracteres = string.ascii_letters +  string.digits + string.punctuation


contrasena = "".join(random.choice(caracteres) for i in range(longintud))

print("La Contraseña es: " + contrasena)

