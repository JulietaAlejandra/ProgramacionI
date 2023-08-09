#Muñoz Julieta Alejandra
'''Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de 
usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento: 
1985 -> Usuario: mfrancisconi, Contraseña: mf.1985.'''

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nacimiento = input("Ingrese su año de nacimiento: ")

usuario = (nombre[0] + apellido).lower()
contrasena = f"{nombre[0]}{apellido[0]}.{nacimiento}"

print("Usuario sugerido:", usuario)
print("Contraseña sugerida:", contrasena)