
'''
import random
listaaleatori = []
listamenu = ["2.- Jugar Adivina numero", "1.- Generar Lista Aleatoria", "0.- Salir del programa"]
menu = -1

while menu != 0:
    Cantidaddeintentos = 5
    Cantidaddeaciertos = 0
    for i in range(len(listamenu)):
        print(listamenu[i])

    menu = int(input("Que desea hacer: "))  

    if menu==1:
        iteraciones = int(input("Ingrese cuantos numeros aleaotrios: "))
        while iteraciones != 0:
            num_ale = random.randint(1, 100)
            listaaleatori.append(num_ale)
            iteraciones-=1
        print(listaaleatori)

    if menu==2:
        if not listaaleatori:
            print("La lista está vacía, llene datos primero")
        else:
            while Cantidaddeintentos != 0:
                numbuscar = int(input("Ingrese numeor a buscar: "))
                if numbuscar in listaaleatori:
                    print("Felicidades encontraste un numero")
                    Cantidaddeaciertos+=1
                else:
                    Cantidaddeintentos-=1
                    print(f"Una menos papám tienes {Cantidaddeintentos} intentos")
                if Cantidaddeaciertos == len(listaaleatori):
                    print("Ganaste el juego")
                    Cantidaddeintentos=0
                elif Cantidaddeintentos == 0:
                    print("Persiste el juego")
'''

import math

def distancia_entre_puntos(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

punto1 = (1, 2)
punto2 = (4, 6)
print("Distancia entre puntos:", distancia_entre_puntos(punto1, punto2))
