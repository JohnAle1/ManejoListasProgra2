# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas pendientes")
    print("4. Salir")
    opcion = input("\nElige una opción: ")
    return opcion

# Lista para almacenar las tareas
tareas = []

# Bucle principal del programa
while True:
    opcion = mostrar_menu()

    if opcion == "1":
        nueva_tarea = input("Ingresa la nueva tarea: ")
        tareas.append({"tarea": nueva_tarea, "completada": False})
        print("Tarea agregada correctamente.")
    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas para marcar como completadas.")
        else:
            print("Tareas Pendientes:")
            for idx, tarea in enumerate(tareas):
                print(f"{idx + 1}. {tarea['tarea']} {'(Completada)' if tarea['completada'] else ''}")
            num_tarea = int(input("Ingresa el número de tarea completada: "))
            if 1 <= num_tarea <= len(tareas):
                tareas[num_tarea - 1]['completada'] = True
                print("Tarea marcada como completada.")
            else:
                print("Número de tarea inválido.")
    elif opcion == "3":
        if len(tareas) == 0:
            print("No hay tareas pendientes.")
        else:
            print("\nTareas Pendientes:")
            for idx, tarea in enumerate(tareas):
                if not tarea['completada']:
                    print(f"{idx + 1}. {tarea['tarea']}")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Inténtalo de nuevo.")
