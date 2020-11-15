from flask import Flask, jsonify, request

from conexion import *

app = Flask(__name__) 

@app.route("/api/v1/usuarios", methods=["POST"])
def usuario():
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
@app.route("/api/v1/peliculas/<int:id>", methods=["GET", "PATCH"])
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

app.run(debug = True)
