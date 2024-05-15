# Definir una función para generar la serie de números triangulares
def numeros_triangulares(n):
    serie = []
    suma = 0
    for i in range(1, n + 1):
        suma += i
        serie.append(suma)
    return serie

# Imprimir los primeros 10 términos de la serie
n = 10
triangulares = numeros_triangulares(n)
print(triangulares)

# Definir una función para generar la serie de cuadrados de números naturales
def cuadrados(n):
    serie = []
    for i in range(1, n + 1):
        serie.append(i ** 2)
    return serie

# Imprimir los primeros 10 términos de la serie
n = 10
cuadrados_naturales = cuadrados(n)
print(cuadrados_naturales)

def collatz(n):
    secuencia = [n]  # Iniciar la secuencia con el número dado
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        secuencia.append(n)  # Agregar el siguiente número a la secuencia
    return secuencia

numero_inicial = 10  # Puedes cambiar este número según tu preferencia
secuencia_collatz = collatz(numero_inicial)
print(secuencia_collatz)


