const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Función para mostrar el menú y obtener la opción del usuario
function mostrarMenu() {
  console.log("\nMenú:");
  console.log("1. Agregar tarea");
  console.log("2. Marcar tarea como completada");
  console.log("3. Mostrar tareas pendientes");
  console.log("4. Salir");
  rl.question("\nElige una opción:", (opcion) => {
    realizarAccion(opcion.trim());
  });
}

// Array para almacenar las tareas
let tareas = [];

// Realizar la acción según la opción elegida
function realizarAccion(opcion) {
  if (opcion === "1") {
    rl.question("Ingresa la nueva tarea:", (nuevaTarea) => {
      tareas.push({ tarea: nuevaTarea, completada: false });
      console.log("Tarea agregada correctamente.");
      mostrarMenu();
    });
  } else if (opcion === "2") {
    if (tareas.length === 0) {
      console.log("No hay tareas para marcar como completadas.");
      mostrarMenu();
    } else {
      console.log("Tareas Pendientes:");
      tareas.forEach((tarea, index) => {
        console.log(
          `${index + 1}. ${tarea.tarea} ${
            tarea.completada ? "(Completada)" : ""
          }`
        );
      });
      rl.question("Ingresa el número de tarea completada:", (numTarea) => {
        numTarea = parseInt(numTarea);
        if (numTarea >= 1 && numTarea <= tareas.length) {
          tareas[numTarea - 1].completada = true;
          console.log("Tarea marcada como completada.");
        } else {
          console.log("Número de tarea inválido.");
        }
        mostrarMenu();
      });
    }
  } else if (opcion === "3") {
    if (tareas.length === 0) {
      console.log("No hay tareas pendientes.");
    } else {
      console.log("\nTareas Pendientes:");
      tareas.forEach((tarea, index) => {
        if (!tarea.completada) {
          console.log(`${index + 1}. ${tarea.tarea}`);
        }
      });
    }
    mostrarMenu();
  } else if (opcion === "4") {
    console.log("¡Hasta luego!");
    rl.close();
  } else {
    console.log("Opción inválida. Inténtalo de nuevo.");
    mostrarMenu();
  }
}

// Iniciar el programa
mostrarMenu();