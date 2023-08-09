#Muñoz Julieta Alejandra
'''Programe una aplicación de consola que pregunte  el precio total de la cuenta, luego 
pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el 
número de comensales y mostrar cuánto debe pagar cada persona.'''

total = float(input("Ingrese el total de la cuenta: "))
comensales = int(input("Cuantos comenzales hay? "))

por_persona = total / comensales

print("Cada uno deberá abonar:", por_persona)