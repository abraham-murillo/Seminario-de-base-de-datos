#ifndef PAQUETERIA_H
#define PAQUETERIA_H

#include <iostream>
#include <deque>
#include "Paquete.h"
using namespace std;

class Paqueteria {
private:
  deque<Paquete> lista;

public: 
  void agregarAlInicio(Paquete paquete);
  void eliminarAlInicio();
  void mostrar();
  void guardar(string archivo);
  void recuperar(string archivo);
};

#endif