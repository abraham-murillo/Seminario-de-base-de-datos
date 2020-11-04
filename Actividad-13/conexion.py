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
