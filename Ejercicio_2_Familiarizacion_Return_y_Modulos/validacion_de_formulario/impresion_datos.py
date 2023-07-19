import validacion_datos as vd

def impresion_datos():
        datos = vd.validacion_datos()
        mensaje = """
        Los datos ingresados son:
        Nombre: {}
        Apellido: {}
        Telefono: {}
        Email: {}
""".format(datos["nombre"], datos["apellido"], datos["telefono"], datos["email"])
        print(mensaje)

if __name__ == "__main__":
        impresion_datos()
