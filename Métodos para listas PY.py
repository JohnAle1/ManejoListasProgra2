# append(elemento): Agrega un elemento al final de la lista.
lista = [1, 2, 3]
lista.append(4)
print(lista)  # Output: [1, 2, 3, 4]

# insert(posición, elemento): Inserta un elemento en la posición especificada.
lista.insert(1, 5)
print(lista)  # Output: [1, 5, 2, 3, 4]

# remove(elemento): Elimina la primera aparición del elemento en la lista.
lista.remove(2)
print(lista)  # Output: [1, 5, 3, 4]

# pop(posición): Elimina y devuelve el elemento en la posición especificada.
elemento_eliminado = lista.pop(2)
print(elemento_eliminado)  # Output: 3
print(lista)  # Output: [1, 5, 4]

# clear(): Elimina todos los elementos de la lista.
lista.clear()
print(lista)  # Output: []

# len(lista): Devuelve la longitud de la lista.
lista = [1, 2, 3, 4, 2]
print(len(lista))  # Output: 5

# count(elemento): Devuelve el número de veces que aparece el elemento en la lista.
print(lista.count(2))  # Output: 2

# index(elemento): Devuelve el índice de la primera aparición del elemento en la lista.
print(lista.index(3))  # Output: 2

# len(lista): Devuelve la longitud de la lista.
lista = [1, 2, 3, 4, 2]
print(len(lista))  # Output: 5

# count(elemento): Devuelve el número de veces que aparece el elemento en la lista.
print(lista.count(2))  # Output: 2

# index(elemento): Devuelve el índice de la primera aparición del elemento en la lista.
print(lista.index(3))  # Output: 2

# copy(): Devuelve una copia superficial de la lista.
nueva_lista = lista.copy()
print(nueva_lista)  # Output: [4, 3, 2, 2, 1]

# extend(iterable): Agrega los elementos de otro iterable al final de la lista actual.
otra_lista = [5, 6, 7]
nueva_lista.extend(otra_lista)
print(nueva_lista)  # Output: [4, 3, 2, 2, 1, 5, 6, 7]

# elemento in lista: Devuelve True si el elemento está en la lista, False en caso contrario.
print(2 in lista)  # Output: True
print(9 in lista)  # Output: False