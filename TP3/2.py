#Muñoz Julieta Alejandra
'''2. Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
Imprimir por pantalla el resultado.'''

numeros = []
for i in range(5):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Ordenar la lista de números
numeros.sort()

# Imprimir el resultado
print("Números ordenados:", numeros)