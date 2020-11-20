from flask import Flask, jsonify, request

from conexion import *

app = Flask(__name__) 

@app.route("/api/v1/usuarios", methods=["POST"])
@app.route("/api/v1/usuarios/<int:id>/peliculas", methods=["GET"])
def usuario(id=None):
  if request.method == "POST" and request.is_json:
    try:
      data = request.get_json()
      print(data)
      
      if crearUsuario(data["correo"], data["contraseña"]):
        return jsonify({"code": "ok"})
      else:
        return jsonify({"code": "existe"})
    except:
      return jsonify({"code": "error"})
  elif request.method == "GET" and id is not None:
    return jsonify(getPeliculasUsuario(id))

@app.route("/api/v1/sesiones", methods=["POST"])
def sesion():
  if request.method == "POST" and request.is_json:
    try:
      data = request.get_json()
      correo = data["correo"]
      contra = data["contraseña"]

      id, ok = iniciarSesion(correo, contra)
      if ok:
        return jsonify({"code": "ok", "id": id})
      else:
        return jsonify({"code": "noExiste"})
    except:
      return jsonify({"code": "error"})

@app.route("/api/v1/peliculas", methods=["GET", "POST"])
@app.route("/api/v1/peliculas/<int:id>", methods=["GET", "PATCH", "DELETE"])
def peliculas(id=None):
  if request.method == "POST" and request.is_json:
    try:
      data = request.get_json()
      print(data)
      if insertarPelicula(data):
        return jsonify({"code": "ok"})
      else:
        return jsonify({"code": "no"})
    except:
      return jsonify({"code": "error"})
  elif request.method == "GET" and id is None:
    return jsonify(getPeliculas())
  elif request.method == "GET" and id is not None:
    return jsonify(getPelicula(id))
  elif request.method == "PATCH" and id is not None and request.is_json:
    data = request.get_json()
    columna = data['columna']
    valor = data['valor']

    if modificarPelicula(id, columna, valor):
      return jsonify(code='ok')
    else:
      return jsonify(code='error')
  elif request.method == "DELETE" and id is not None:
    if eliminarPelicula(id):
      return jsonify(code='ok')
    else:
      return jsonify(code='error')

app.run(debug = True)
