def mensaje_bienvenida():
    "Esta funcion es para dar la bienvenida al programa y para dar el saludo general"
    nombre_programa = "Contraseña Segura"
    mensaje = """
    ---------------------------------
    Bienvenidos al programa {}
    ---------------------------------
    Este programa sirve para ingresar una contraseña y verificar si es segura.
""".format(nombre_programa)
    print(mensaje)
    