#Muñoz Julieta Alejandra
'''Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al 
derecho que al revés. Por ejemplo: rayar, kayak, somos.'''

texto = input("Ingrese un texto: ")

#Quita espacios en blanco y convierte el texto a minúsculas
texto = texto.replace(" ", "").lower()

texto_al_reves = texto[::-1]

if texto == texto_al_reves:
    print("El texto es un palíndromo.")
else:
    print("El texto no es un palíndromo.")