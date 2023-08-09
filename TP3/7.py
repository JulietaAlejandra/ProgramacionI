#Muñoz Julieta Alejandra
'''7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al
usuario:
a. Agregar nuevas tareas pendientes.
b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
de la lista de pendientes a la de terminadas.
Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas
listas.'''
#Mostrar el estado de las listas
def mostrar_estado_listas(pendientes, terminadas):
    print("Tareas pendientes:", pendientes)
    print("Tareas terminadas:", terminadas)

# Listas iniciales - vacias
tareas_pendientes = []
tareas_terminadas = []

while True:
    # Mostrar estado actual de las listas
    mostrar_estado_listas(tareas_pendientes, tareas_terminadas)

    # Menu
    print("Opciones:")
    print("A. Agregar nueva tarea pendiente")
    print("B. Marcar tarea pendiente como terminada")
    print("C. Salir")
    op = input("Seleccione una opción: ")
    opcion = op.capitalize()

    if opcion == 'A':
        nueva_tarea = input("Ingrese la nueva tarea pendiente: ")
        tareas_pendientes.append(nueva_tarea)
    elif opcion == 'B':
        if len(tareas_pendientes) == 0:
            print("No hay tareas pendientes para marcar como terminadas.")
        else:
            tarea_a_terminar = input("Ingrese la tarea que desea marcar como terminada: ")
            if tarea_a_terminar in tareas_pendientes:
                tareas_pendientes.remove(tarea_a_terminar)
                tareas_terminadas.append(tarea_a_terminar)
                print("Tarea marcada como terminada.")
            else:
                print("La tarea no se encuentra en la lista de pendientes.")
    elif opcion == 'C':
        print("SALIENDO...")
        break
    else:
        print("Opción inválida. Por favor, seleccione A, B o C.")