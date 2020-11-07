import mysql.connector

bd = mysql.connector.connect(
  user='abraham', password='123', database='cinemapp')

cursor = bd.cursor()

def getUsuarios():
  consulta = "SELECT * FROM usuario"

  cursor.execute(consulta)
  usuarios = []
  for row in cursor.fetchall():
    usuario = {
      'id': row[0],
      'correo': row[1],
      'contraseña': row[2]
    }
    usuarios.append(usuario)
  return usuarios

def existeUsuario(correo):
  query = "SELECT COUNT(*) FROM usuario WHERE correo = %s"
  cursor.execute(query, (correo, ))

  if cursor.fetchone()[0] == 1:
    return True
  else:
    return False

import hashlib
def crearUsuario(correo, contra):
  if existeUsuario(correo):
    return False
  else:
    h = hashlib.new("sha256", bytes(contra, "utf-8"))
    h = h.hexdigest()
    insertar = "INSERT INTO usuario(correo, contraseña) VALUES (%s, %s)"
    cursor.execute(insertar, (correo, h))
    bd.commit()

    return True

def iniciarSesion(correo, contra):
  h = hashlib.new("sha256", bytes(contra, "utf-8"))
  h = h.hexdigest()
  query = "SELECT id FROM usuario WHERE correo = %s AND contraseña = %s"
  cursor.execute(query, (correo, h))
  id = cursor.fetchone()
  if id:
      return id[0], True
  else:
      return None, False
