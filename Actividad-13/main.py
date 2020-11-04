from flask import Flask, jsonify
from conexion import getUsuarios

app = Flask(__name__)

@app.route("/")
def hola():
  return "<b>Hola mundo!<b>"

# @app.route("/usuarios/<string:nombre>")
# def usuarios(nombre):
#   return "Hola %s" % nombre

@app.route("/api/v1/usuarios")
def usuarios():
  usuariosList = getUsuarios()
  # usuario = {
  #   'id': 10,
  #   'correo': 'abraham@gmail.com',
  #   'contraseña': '12345678'
  # }
  # usuariosList.append(usuario)
  return jsonify(usuariosList)

app.run()

