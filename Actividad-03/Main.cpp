#include <bits/stdc++.h>
#include "Paquete.h"
#include "Paqueteria.cpp"
#include <fstream>
using namespace std;

// Abraham Baltazar Murillo Sandoval

int main() {

  Paqueteria paqueteria;
  enum Operaciones {Agregar = '1', Eliminar, Mostrar, Guardar, Recuperar, Salir = 'x'};
  char operacion;
  string archivo = "Paqueteria.txt";

  do {
    cout << "\n---------------\n";
    cout << "Paqueteria\n";
    cout << "1.- Agregar paquete\n";
    cout << "2.- Eliminar paquete\n";
    cout << "3.- Mostrar\n"; 
    cout << "4.- Guardar\n";
    cout << "5.- Recuperar\n";
    cout << "x.- Salir\n";

    cin >> operacion;
    switch (operacion) {
      case Agregar : {
        Paquete paquete;
        cin >> paquete;
        paqueteria.agregarAlInicio(paquete);
        break;
      }
      
      case Eliminar : {
        paqueteria.eliminarAlInicio();
        break;
      }

      case Mostrar : {
        paqueteria.mostrar();
        break;
      }

      case Guardar : {
        paqueteria.guardar(archivo);
        break;
      }

      case Recuperar : {
        paqueteria.recuperar(archivo);
        break;
      }

      case Salir : {
        cout << "Hasta luego\n";
        break;
      }

      default:
        cout << "operacion invalida\n";
        break;
    }
  } while (operacion != Salir);

  return 0;
} 

/*
1- Agregar paquete: crea un objeto de la clase `Paquete` y lo inserta en la lista simplemente ligada (`Paquetería`).
2- Eliminar paquete: elimina el paquete que se encuentra al inicio de la lista de la Paquetería.
3- Mostrar: recorre la lista mostrando los datos de cada paquete.
4- Guardar: crear un archivo .txt con la información de todos los paquetes de la Paquetería (respaldar)
5- Recuperar: carga a la Paquetería los paquetes repaldados en el archivo .txt
*/
