#include "Paqueteria.h"
#include <fstream>
using namespace std;

void Paqueteria::agregarAlInicio(Paquete paquete) {
  this->lista.push_front(paquete);
  cout << "Elemento agregado correctamente\n";
}

void Paqueteria::eliminarAlInicio() {
  if (this->lista.empty()) {
    cout << "No hay elementos en la paqueteria para eliminar\n";
  } else {
    this->lista.pop_front();
    cout << "Elemento eliminado satisfactoriamente\n";
  }
}

void Paqueteria::mostrar() {
  if (this->lista.empty()) {
    cout << "No hay elementos para mostrar\n";
  } else {
    cout << "La paqueteria tiene los siguientes paquetes: \n";
    for (auto x : this->lista) {
      cout << "Id : " << x.getId() << ", ";
      cout << "Origen : " << x.getOrigen() << ", ";
      cout << "Destino : " << x.getDestino() << ", ";
      cout << "Peso : " << x.getPeso() << '\n';
    }
  }
}

void Paqueteria::guardar(string archivo) {
  ofstream salida(archivo.c_str());
  salida << lista.size() << '\n';
  for (auto x : this->lista) {
    salida << x.getId() << " " << x.getOrigen() << " " << x.getDestino() << " " << x.getPeso() << '\n';
  }
  salida.close();
}

void Paqueteria::recuperar(string archivo) {
  ifstream entrada(archivo.c_str());
  this->lista.clear();
  int n;
  entrada >> n;
  while (n--) {
    Paquete x;
    entrada >> x;
    this->lista.push_back(x);
  } 
  entrada.close();
}


