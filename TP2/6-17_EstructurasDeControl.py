#Muñoz Julieta Alejandra
'''En esta segunda parte deberán utilizar estructuras de control condicionales (y en lo posible y dado el
caso funciones) para escribir programas que lleven a cabo lo siguiente:
6. Que pida al usuario una palabra y la muestre por pantalla 10 veces.'''

def mostrar_palabra(palabra, veces):
    for i in range(veces):
        print(palabra)

#Llamado y test
print("----------PUNTO6----------")
palabra_usuario = input("Ingrese una palabra: ")
mostrar_palabra(palabra_usuario, 10)


####################################################
'''7. Que imprima todos los números entre el 100 y el 199.'''

def imprimir_numeros_entre(minimo, maximo):
    for numero in range(minimo, maximo + 1):
        print(numero)

#Llamado y test
print("\n----------PUNTO7----------")
imprimir_numeros_entre(100, 199)


####################################################
'''8. Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.'''

def mayor_edad(edad):
    if edad >= 18:
        print("Es mayor de edad.")
    else:
        print("No es mayor de edad.")

#Llamado y test
print("\n----------PUNTO8----------")
edad_usuario = int(input("Ingrese su edad: "))
mayor_edad(edad_usuario)


####################################################
'''9. Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso
en que ambos números son iguales.'''

def encontrar_menor(num1, num2):
    if num1 < num2:
        return num1
    elif num2 < num1:
        return num2
    else:
        return "Son iguales"

#Llamado y test
print("\n----------PUNTO9----------")
numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))

resultado = encontrar_menor(numero1, numero2)
print(f"El menor número es: {resultado}")


####################################################
'''10. Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
a. Todos los números impares desde 1 hasta ese número separados por comas.
b. La cuenta atrás desde ese número hasta cero separados por comas.
c. Que indique si es primo o no.
d. Por último, su factorial.'''

def numeros(numero_entero_positivo):
    #a
    for i in range(1, numero_entero_positivo + 1):
        if i % 2 != 0:
            print(i, end=", ")
    #b
    print("")
    for i in range(numero_entero_positivo, -1, -1):
        print(i, end=", ")
    #c
    if numero_entero_positivo % 2 != 0:
        print("\nEl numero es primo")
    else:
        print("\nEl numero no es primo")
    #d
    factorial = 1
    for i in range(1, numero_entero_positivo + 1):
        factorial = factorial * i
    print("El factorial es: " + str(factorial))

#Llamado y test
print("\n----------PUNTO10----------")
numero_entero_positivo = int(input("Ingrese un numero entero positivo: "))
numeros(numero_entero_positivo)


####################################################
'''11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
encuentran en dicha frase.'''

def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    cantidad_vocales = 0
    for caracter in frase:
        if caracter in vocales:
            cantidad_vocales += 1
    return cantidad_vocales

#Llamado y test
print("\n----------PUNTO11----------")
frase_usuario = input("Ingrese una frase: ")
cantidad_vocales = contar_vocales(frase_usuario)
print(f"La cantidad de vocales en la frase es: {cantidad_vocales}")


####################################################
'''12. Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
ingresado no es ninguno de esos, imprimir otro mensaje.'''

def verificar_dia_semana(dia):
    if dia.lower() == "lunes":
        print("Es lunes, BUEN COMIENZO DE SEMANA😀.")
    elif dia.lower() == "viernes":
        print("Es viernes y tu cuerpo lo sabe!💃🏽")
    elif dia.lower() == "sábado" or dia.lower() == "domingo":
        print("Es fin de semana... A DISFRUTAR!")
    else:
        print("Un día más.💪🏽")

#Llamado y test
print("\n----------PUNTO12----------")
dia = input("Ingrese un día de la semana: ")
verificar_dia_semana(dia)


####################################################
'''13. Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos
A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un
nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla
el grupo que le corresponde.'''

def determinar_grupo(nombre, sexo):
    if (sexo.lower() == "mujer" and nombre.lower() < 'm') or (sexo.lower() == "hombre" and nombre.lower() > 'n'):
        return "A"
    else:
        return "B"

#Llamado y test
print("\n----------PUNTO13----------")
nombre_alumno = input("Ingrese su nombre: ")
sexo_alumno = input("Ingrese su sexo (Mujer/Hombre): ")

grupo = determinar_grupo(nombre_alumno, sexo_alumno)
print(f"Usted pertenece al grupo: {grupo}")


####################################################
'''14. Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son
múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos
ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900
no es bisiesto.'''

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print(f"{anio} es bisiesto.")
    else:
        print(f"{anio} no es bisiesto.")

#Llamado y test
print("\n----------PUNTO14----------")
anio = int(input("Ingrese un año: "))
es_bisiesto(anio)


####################################################
'''15. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe
validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
informarle que no se puede procesar el dato.'''

def es_vocal(letra):
    vocales = "aeiouAEIOU"
    if len(letra) == 1:
        if letra in vocales:
            print("Es vocal.")
        else:
            print("No es vocal.")
    else:
        print("No se puede procesar el dato ingresado.")

#Llamado y test
print("\n----------PUNTO15----------")
letra_ingresada = input("Ingrese una letra: ")
es_vocal(letra_ingresada)


####################################################
'''16. Que imprima el siguiente patrón:
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1'''

n = 5

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

####################################################
'''17. Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay.'''
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

#Llamado y test
print("\n----------PUNTO17----------")
numeros_primos = [num for num in range(0, 101) if es_primo(num)]

print("Números primos entre 0 y 100:", ", ".join(map(str, numeros_primos)))
print("Cantidad de números primos:", len(numeros_primos))