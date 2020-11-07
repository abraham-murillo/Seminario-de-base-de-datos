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

app.run(debug=True)
