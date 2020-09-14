#ifndef PAQUETE_H
#define PAQUETE_H

#include <iostream>
#include <fstream>
using namespace std;

class Paquete {
private:
  int id;
  string origen;
  string destino;
  double peso;

public:
  int getId() const { return id; }
  string getOrigen() const { return origen; }
  string getDestino() const { return destino; }
  double getPeso() const { return peso; }

  void setId(const int& x) { id = x; }
  void setOrigen(const string& x) { origen = x; }
  void setDestino(const string& x) { destino = x; }
  void setPeso(const double& x) { peso = x; }

  explicit Paquete(int id = 0, string origen = "", string destino = "", double peso = 0.0) : 
    id(id), origen(origen), destino(destino), peso(peso) {}

  friend istream& operator >> (istream &is, Paquete& p) {
    int id;
    cout << "Ingrese el id: ";
    is >> id;
    p.setId(id);

    string origen;
    cout << "Ingrese el origen: ";
    is >> origen;
    p.setOrigen(origen);

    string destino;
    cout << "Ingrese el destino: ";
    is >> destino;
    p.setDestino(destino);

    double peso;
    cout << "Ingrese el peso: ";
    is >> peso;
    p.setPeso(peso);

    return is;
  }
};

#endif