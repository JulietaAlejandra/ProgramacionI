#Muñoz Julieta Alejandra
'''Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y 
luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente 
forma: “La respuesta es XX”.'''

num = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro: "))
num3 = int(input("Ingrese otro más: "))

suma = num + num2
multiplicar = suma * num3

print("El la respuesta es:", multiplicar)