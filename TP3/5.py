#Muñoz Julieta Alejandra
'''5. Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos.  Cada uno
de los números ingresados por el usuario deberá ser almacenado en una lista. A
continuación, realice las siguientes tareas:'''

#Obtener números enteros del usuario y almacenarlos en una lista
def obtener_numeros():
    numeros = []
    while True:
        entrada = input("Ingrese un número entero o 'fin' para terminar: ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Ingrese un número entero o 'fin'.")
    return numeros

#Obtener números
numeros_ingresados = obtener_numeros()
print("\nLista de números ingresados:", numeros_ingresados)

###########################################################
'''a. Determinar el máximo.'''

def maximo_valor(lista):
    return max(lista)

print("\n-----A-----")
print("Máximo valor:", maximo_valor(numeros_ingresados))

###########################################################
'''b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.'''

def segundo_maximo(lista):
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada[1]

print("\n-----B-----")
print("Segundo valor máximo:", segundo_maximo(numeros_ingresados))

###########################################################
'''c. Determinar el mínimo.'''

def minimo_valor(lista):
    return min(lista)

print("\n-----C-----")
print("Mínimo valor:", minimo_valor(numeros_ingresados))

###########################################################
'''d. Calcular la multiplicación de  todos los números de la lista.'''

def multiplicacion_valores(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

print("\n-----D-----")
print("Multiplicación de todos los números:", multiplicacion_valores(numeros_ingresados))

###########################################################
'''e. Contar los valores pares e impares.'''

def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

print("\n-----E-----")
pares, impares = contar_pares_impares(numeros_ingresados)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)

###########################################################
'''f. Remover los elementos repetidos.'''

def eliminar_repetidos(lista):
    lista_sin_repetidos = list(set(lista))
    return lista_sin_repetidos

print("\n-----F-----")
numeros_sin_repetidos = eliminar_repetidos(numeros_ingresados)
print("Lista sin elementos repetidos:", numeros_sin_repetidos)