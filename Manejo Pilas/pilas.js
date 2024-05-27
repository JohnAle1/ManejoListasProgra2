// Importar la pila desde ds.js
const { Stack } = require('@datastructures-js/stack');

// Crear una nueva instancia de la pila
const stack = new Stack();

// 1. push(element)
// Agregar elementos a la pila
stack.push(10);
stack.push(20);
stack.push(30);
console.log("Después de push: ", stack); // Salida: Stack { items: [ 10, 20, 30 ] }

// 2. pop()
// Obtener y eliminar el elemento superior de la pila
const poppedElement = stack.pop(); // Elimina 30
console.log("Elemento eliminado con pop: ", poppedElement); // Salida: 30
console.log("Después de pop: ", stack); // Salida: Stack { items: [ 10, 20 ] }

// 3. peek()
// Obtener el elemento superior sin eliminarlo
const topElement = stack.peek(); // Obtiene 20
console.log("Elemento superior con peek: ", topElement); // Salida: 20
console.log("Después de peek: ", stack); // Salida: Stack { items: [ 10, 20 ] }

// 4. isEmpty()
// Verificar si la pila está vacía
const isEmpty = stack.isEmpty(); // Devuelve false
console.log("La pila está vacía: ", isEmpty); // Salida: false

// 5. size()
// Obtener el tamaño de la pila
const size = stack.size(); // Devuelve 2
console.log("Tamaño de la pila: ", size); // Salida: 2

// 6. clear()
// Vaciar la pila
stack.clear();
console.log("Después de clear: ", stack); // Salida: Stack { items: [] }
