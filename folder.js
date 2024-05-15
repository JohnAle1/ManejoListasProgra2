const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let menu = -1;

rl.on("line", (input) => {
  if (menu === 0) {
    rl.close();
    return;
  }

  switch (menu) {
    case 1:
      const iteraciones = parseInt(input);
      for (let i = 0; i < iteraciones; i++) {
        const numAleatorio = Math.floor(Math.random() * 100) + 1;
        listaaleatoria.push(numAleatorio);
      }
      console.log("Lista aleatoria generada:", listaaleatoria);
      break;
    case 2:
      if (listaaleatoria.length === 0) {
        console.log("La lista está vacía, genere una lista primero.");
      } else {
        let cantidadIntentos = 5;
        let cantidadAciertos = 0;
        while (cantidadIntentos > 0) {
          rl.question("Ingrese número a buscar: ", (numBuscar) => {
            numBuscar = parseInt(numBuscar);
            if (listaaleatoria.includes(numBuscar)) {
              console.log("¡Felicidades! Encontraste un número.");
              cantidadAciertos++;
            } else {
              cantidadIntentos--;
              console.log(
                `No es correcto. Te quedan ${cantidadIntentos} intentos.`
              );
            }

            if (cantidadAciertos === listaaleatoria.length) {
              console.log("¡Ganaste el juego!");
              cantidadIntentos = 0;
            } else if (cantidadIntentos === 0) {
              console.log("Se acabaron los intentos. Persiste el juego.");
            }
          });
        }
      }
      break;
    default:
      console.log("Opción no válida.");
      break;
  }

  for (let i = 0; i < listamenu.length; i++) {
    console.log(listamenu[i]);
  }

  rl.question("¿Qué desea hacer?: ", (answer) => {
    menu = parseInt(answer);
  });
});

console.log("Bienvenido al programa");
