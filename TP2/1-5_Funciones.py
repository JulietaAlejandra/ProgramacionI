#Muñoz Julieta Alejandra
'''En cada ejercicio deberán escribir un programa utilizando una función que haga lo siguiente:
1. Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!.'''

def saludar(nombre):
    print(f"¡Hola {nombre}!")

#Llamado y test de funcion.
print("----------PUNTO1----------")
nombre_usuario = input("Ingrese su nombre: ")
saludar(nombre_usuario)


####################################################
'''2. Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado'''

def calcular_potencia(base, exponente):
    resultado = base ** exponente
    return resultado

#Llamado y test de funcion.
print("\n----------PUNTO2----------")
numero = int(input("Ingrese un número entero: "))
potencia = int(input("Ingrese la potencia a la que desea elevarlo: "))
resultado_potencia = calcular_potencia(numero, potencia)
print(f"{numero} elevado a la {potencia} es igual a {resultado_potencia}")


####################################################
'''3. Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y
el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA,
se deberá aplicar un 21%'''

def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    total_factura = cantidad_sin_iva + iva
    return total_factura

#Llamado y test de funcion.
print("\n----------PUNTO3----------")
cantidad_sin_iva = float(input("Ingrese la cantidad sin IVA: "))
porcentaje_iva = float(input("Ingrese el porcentaje de IVA (opcional, presione Enter para aplicar el 21%): ") or 21)

total = calcular_total_factura(cantidad_sin_iva, porcentaje_iva)
print(f"El total de la factura con IVA es: {total}")


####################################################
'''4. Que dada la base y altura de un triángulo nos calcule su área'''

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

#Llamado y test de funcion.
print("\n----------PUNTO4----------")
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = area_triangulo(base, altura)
print(f"El área del triángulo es: {area}")


####################################################
'''5. Que dado tres números ingresados por el usuario nos devuelva el promedio'''

def cal_promedio(num1, num2, num3):
    promedio = (num1 + num2 + num3) / 3
    return promedio

#Llamado y test de funcion.
print("\n----------PUNTO5----------")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = cal_promedio(num1, num2, num3)
print(f"El promedio de los tres números es: {promedio}")