#Muñoz Julieta Alejandra
'''3. Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
debajo la misma lista pero sólo con las frutas que añadió el usuario.'''

# Lista de frutas
frutas = ["banana", "manzana", "pera"]

# Solicitar que se ingresen 3 frutas adicionales y agregarlas a la lista
for i in range(3):
    fruta = input(f"Ingrese una fruta: ")
    frutas.append(fruta)

# Mostrar la lista completa
print("Lista completa de frutas:", frutas)

# Mostrar la lista con las frutas agregadas por el usuario
frutas_agregadas = frutas[3:]  # Obtener las frutas agregadas al final
print("Frutas agregadas por el usuario:", frutas_agregadas)