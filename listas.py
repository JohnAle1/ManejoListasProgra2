#Clase para crear un nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
#Clase para crear la lista base enlazada simple
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def insertar_despues(self, dato_referencia, dato_nuevo):
        actual = self.cabeza
        while actual:
            if actual.dato == dato_referencia:
                nuevo_nodo = Nodo(dato_nuevo)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return
            actual = actual.siguiente
        print(f"Dato de referencia {dato_referencia} no encontrado en la lista.")

    def eliminar(self, dato):
        if self.cabeza is None:
            print("Lista vacía, nada que eliminar.")
            return
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente
        print(f"Dato {dato} no encontrado en la lista.")

    def obtener_longitud(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def obtener_inicio(self):
        if self.cabeza:
            return self.cabeza.dato
        return None

    def obtener_final(self):
        if self.cabeza is None:
            return None
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        return actual.dato

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

    def vaciar(self):
        self.cabeza = None

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar_inicio(3)
lista.insertar_inicio(6)
lista.insertar_final(9)
lista.insertar_inicio(1)

print("Lista original:")
lista.imprimir_lista()

lista.insertar_despues(6, 7)
lista.eliminar(3)

print("\nLista modificada:")
lista.imprimir_lista()

print(f"\nLongitud de la lista: {lista.obtener_longitud()}")
print(f"Dato al inicio de la lista: {lista.obtener_inicio()}")
print(f"Dato al final de la lista: {lista.obtener_final()}")

print("\nBuscar elementos:")
print(f"¿El dato 6 está en la lista? {lista.buscar(6)}")
print(f"¿El dato 10 está en la lista? {lista.buscar(10)}")

lista.vaciar()
print("\nLista después de vaciar:")
lista.imprimir_lista()