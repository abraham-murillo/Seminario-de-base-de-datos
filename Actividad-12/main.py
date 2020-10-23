import mysql.connector

bd = mysql.connector.connect(
  user='abraham', password='123', database='nopalito')

cursor = bd.cursor()

while True:
  print("1) Agregar usuario")
  print("2) Mostrar usuarios")
  print("0) Salir")
  op = input()

  if op == '1':
    nombre = input("nombre: ")
    edad = input("edad: ")
    sexo = input("sexo: ")
    direccion = input("direccion: ")

    consulta = "INSERT INTO usuario(nombre, edad, sexo, direccion) VALUES (%s, %s, %s, %s)"
    cursor.execute(consulta, (nombre, edad, sexo, direccion))
    bd.commit()

    if cursor.rowcount:
      print("Se agregó el usuario correctamente")
    else:
      print("Error :c")

  elif op == '2':
    consulta = "SELECT * FROM usuario"

    cursor.execute(consulta)
    for row in cursor.fetchall():
      print("id:", row[0])
      print("nombre:", row[1])
      print("edad:", row[2])
      print("sexo:", row[3])
      print("dirección:", row[4])
      print()

  else:
    break
  print()

bd.close()