from collections import deque

# Crear un deque vacío
stack = deque()

# 1. append(x): Añade el elemento `x` al final del deque
stack.append(1)
stack.append(2)
stack.append(3)
print(f"Después de append: {stack}")  # deque([1, 2, 3])

# 2. appendleft(x): Añade el elemento `x` al inicio del deque
stack.appendleft(0)
print(f"Después de appendleft: {stack}")  # deque([0, 1, 2, 3])

# 3. pop(): Elimina y devuelve el último elemento del deque
last_element = stack.pop()
print(f"Elemento eliminado con pop: {last_element}")  # 3
print(f"Después de pop: {stack}")  # deque([0, 1, 2])

# 4. popleft(): Elimina y devuelve el primer elemento del deque
first_element = stack.popleft()
print(f"Elemento eliminado con popleft: {first_element}")  # 0
print(f"Después de popleft: {stack}")  # deque([1, 2])

# 5. clear(): Elimina todos los elementos del deque
stack.clear()
print(f"Después de clear: {stack}")  # deque([])

# Añadiendo elementos de nuevo para los siguientes ejemplos
stack.extend([1, 2, 3])
print(f"Después de extend([1, 2, 3]): {stack}")  # deque([1, 2, 3])

# 6. extend(iterable): Añade los elementos del iterable al final del deque
stack.extend([4, 5, 6])
print(f"Después de extend([4, 5, 6]): {stack}")  # deque([1, 2, 3, 4, 5, 6])

# 7. extendleft(iterable): Añade los elementos del iterable al inicio del deque (en orden inverso)
stack.extendleft([-1, -2, -3])
print(f"Después de extendleft([-1, -2, -3]): {stack}")  # deque([-3, -2, -1, 1, 2, 3, 4, 5, 6])

# 8. remove(value): Elimina la primera aparición de `value` en el deque
stack.remove(3)
print(f"Después de remove(3): {stack}")  # deque([-3, -2, -1, 1, 2, 4, 5, 6])

# 9. count(value): Devuelve el número de veces que `value` aparece en el deque
contador = stack.count(1)
print(f"El número 1 aparece {contador} vez/veces en el deque")  # 1

# 10. index(value, start=0, stop=len(deque)): Devuelve el índice de la primera aparición de `value` entre las posiciones `start` y `stop`
index_of_4 = stack.index(4)
print(f"El índice de la primera aparición del número 4 es: {index_of_4}")  # 4

# Estado final del deque
print(f"Estado final del deque: {stack}")  # deque([-2, -1, 1, 2, 4, 5, 6, -3])
