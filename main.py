import random

print("=== GENERADOR DE CONTRASEÑAS ===")

longitud = int(input("Ingrese la longitud de la contraseña: "))

usar_numeros = input("¿Desea incluir números? (s/n): ")
usar_mayusculas = input("¿Desea incluir mayúsculas? (s/n): ")

letras = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

caracteres = letras

if usar_numeros == "s":
    caracteres = caracteres + numeros

if usar_mayusculas == "s":
    caracteres = caracteres + mayusculas

contrasena = ""

for i in range(longitud):
    contrasena = contrasena + random.choice(caracteres)

print("Contraseña generada:")
print(contrasena)