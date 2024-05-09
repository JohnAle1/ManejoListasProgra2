class Nodo {
  constructor(dato) {
    this.dato = dato;
    this.siguiente = null;
  }
}

class ListaEnlazada {
  constructor() {
    this.cabeza = null;
  }

  insertarInicio(dato) {
    let nuevoNodo = new Nodo(dato);
    nuevoNodo.siguiente = this.cabeza;
    this.cabeza = nuevoNodo;
  }

  insertarFinal(dato) {
    let nuevoNodo = new Nodo(dato);
    if (!this.cabeza) {
      this.cabeza = nuevoNodo;
      return;
    }
    let actual = this.cabeza;
    while (actual.siguiente) {
      actual = actual.siguiente;
    }
    actual.siguiente = nuevoNodo;
  }

  insertarDespues(datoReferencia, datoNuevo) {
    let actual = this.cabeza;
    while (actual) {
      if (actual.dato === datoReferencia) {
        let nuevoNodo = new Nodo(datoNuevo);
        nuevoNodo.siguiente = actual.siguiente;
        actual.siguiente = nuevoNodo;
        return;
      }
      actual = actual.siguiente;
    }
    console.log(
      `Dato de referencia ${datoReferencia} no encontrado en la lista.`
    );
  }

  eliminar(dato) {
    if (!this.cabeza) {
      console.log("Lista vacía, nada que eliminar.");
      return;
    }
    if (this.cabeza.dato === dato) {
      this.cabeza = this.cabeza.siguiente;
      return;
    }
    let actual = this.cabeza;
    while (actual.siguiente) {
      if (actual.siguiente.dato === dato) {
        actual.siguiente = actual.siguiente.siguiente;
        return;
      }
      actual = actual.siguiente;
    }
    console.log(`Dato ${dato} no encontrado en la lista.`);
  }

  obtenerLongitud() {
    let contador = 0;
    let actual = this.cabeza;
    while (actual) {
      contador++;
      actual = actual.siguiente;
    }
    return contador;
  }

  buscar(dato) {
    let actual = this.cabeza;
    while (actual) {
      if (actual.dato === dato) {
        return true;
      }
      actual = actual.siguiente;
    }
    return false;
  }

  obtenerInicio() {
    return this.cabeza ? this.cabeza.dato : null;
  }

  obtenerFinal() {
    if (!this.cabeza) {
      return null;
    }
    let actual = this.cabeza;
    while (actual.siguiente) {
      actual = actual.siguiente;
    }
    return actual.dato;
  }

  imprimirLista() {
    let actual = this.cabeza;
    while (actual) {
      process.stdout.write(`${actual.dato} -> `);
      actual = actual.siguiente;
    }
    console.log("null");
  }

  vaciar() {
    this.cabeza = null;
  }
}

// Ejemplo de uso
let lista = new ListaEnlazada();
lista.insertarInicio(3);
lista.insertarInicio(6);
lista.insertarFinal(9);
lista.insertarInicio(1);

console.log("Lista original:");
lista.imprimirLista();

lista.insertarDespues(6, 7);
lista.eliminar(3);

console.log("\nLista modificada:");
lista.imprimirLista();

console.log(`\nLongitud de la lista: ${lista.obtenerLongitud()}`);
console.log(`Dato al inicio de la lista: ${lista.obtenerInicio()}`);
console.log(`Dato al final de la lista: ${lista.obtenerFinal()}`);

console.log("\nBuscar elementos:");
console.log(`¿El dato 6 está en la lista? ${lista.buscar(6)}`);
console.log(`¿El dato 10 está en la lista? ${lista.buscar(10)}`);

lista.vaciar();
console.log("\nLista después de vaciar:");
lista.imprimirLista();
