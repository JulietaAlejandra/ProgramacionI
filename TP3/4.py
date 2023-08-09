#Muñoz Julieta Alejandra
'''4. Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”],
realizar lo siguiente:'''

paises = ["Argentina", "Brasil", "Bolivia", "Paraguay", "Venezuela"]
print("Esta es la lista inicial de paises:", paises)

###############################################
'''a. Imprimir la cantidad de elementos que tiene la lista.'''

def imprimir_cantidad(lista):
    print("\n------PUNTO A------")
    print("Cantidad de elementos en la lista:", len(lista))

imprimir_cantidad(paises)

###############################################
'''b. Imprimir el primer y último elemento.'''

def imprimir_primer_ultimo(lista):
    print("\n------PUNTO B-----")
    print("Primer elemento:", lista[0])
    print("Último elemento:", lista[-1])

imprimir_primer_ultimo(paises)

###############################################
'''c. Imprimir el resto.'''

def imprimir_resto(lista):
    print("\n------PUNTO C------")
    print("Resto de elementos:", lista[1:-1])

imprimir_resto(paises)

###############################################
'''d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista. Si no se encuentra,
imprimir un mensaje advirtiendo al usuario.'''

def buscar_pais_indice(lista, pais_buscar):
    print("\n------PUNTO D------")
    if pais_buscar in lista:
        indice = lista.index(pais_buscar)
        print(f"El país '{pais_buscar}' se encuentra en el índice {indice}.")
    else:
        print(f"El país '{pais_buscar}' no se encuentra en la lista.")

pais_a_buscar = input("Ingrese un país para buscar: ")
buscar_pais_indice(paises, pais_a_buscar)

###############################################
'''e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista.
Quitar el elemento correspondiente de esa posición.'''

def eliminar_por_indice(lista, indice):
    print("\n------PUNTO E------")
    if 0 <= indice < len(lista):
        pais_eliminado = lista.pop(indice)
        print(f"Se eliminó el país '{pais_eliminado}' de la lista.")
    else:
        print("Número inválido.")

indice_a_eliminar = int(input(f"Ingrese un número entre 1 y {len(paises)} para eliminar un país: ")) - 1
eliminar_por_indice(paises, indice_a_eliminar)

###############################################
'''f. Imprimir la lista en orden inverso.'''

def imprimir_lista_inversa(lista):
    print("\n------PUNTO F------")
    lista_inversa = lista[::-1]
    print("Lista en orden inverso:", lista_inversa)

imprimir_lista_inversa(paises)

###############################################
'''g. Vaciar la lista.'''

def vaciar_lista(lista):
    print("\n------PUNTO G------")
    lista.clear()
    print("Lista vaciada:", lista)

vaciar_lista(paises)