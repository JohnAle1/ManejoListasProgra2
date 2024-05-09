// push(elemento): Agrega un elemento al final del array.
let array = [1, 2, 3];
array.push(4);
console.log(array); // Output: [1, 2, 3, 4]

// splice(posición, 0, elemento): Inserta un elemento en la posición especificada.
array.splice(1, 0, 5);
console.log(array); // Output: [1, 5, 2, 3, 4]

// indexOf(elemento): Devuelve el índice de la primera aparición del elemento en el array.
let index = array.indexOf(2);

// splice(posición, cantidad): Elimina elementos en la posición especificada.
array.splice(index, 1);
console.log(array); // Output: [1, 5, 3, 4]

// pop(): Elimina y devuelve el último elemento del array.
let elementoEliminado = array.pop();
console.log(elementoEliminado); // Output: 4
console.log(array); // Output: [1, 5, 3]

// splice(0, array.length): Elimina todos los elementos del array.
array.splice(0, array.length);
console.log(array); // Output: []

// length: Devuelve la longitud del array.
array = [1, 2, 3, 4, 2];
console.log(array.length); // Output: 5

// filter(elemento): Devuelve un nuevo array con los elementos que cumplen la condición.
let filteredArray = array.filter(num => num === 2);
console.log(filteredArray.length); // Output: 2

// indexOf(elemento): Devuelve el índice de la primera aparición del elemento en el array.
console.log(array.indexOf(3)); // Output: 2

// sort(): Ordena el array de forma ascendente.
array.sort();
console.log(array); // Output: [1, 2, 2, 3, 4]

// reverse(): Invierte el orden de los elementos en el array.
array.reverse();
console.log(array); // Output: [4, 3, 2, 2, 1]

// slice(): Devuelve una copia superficial del array.
let newArray = array.slice();
console.log(newArray); // Output: [4, 3, 2, 2, 1]

// concat(array): Une dos arrays.
let anotherArray = [5, 6, 7];
newArray = newArray.concat(anotherArray);
console.log(newArray); // Output: [4, 3, 2, 2, 1, 5, 6, 7]

// includes(elemento): Devuelve true si el elemento está en el array, false en caso contrario.
console.log(array.includes(2)); // Output: true
console.log(array.includes(9)); // Output: false
