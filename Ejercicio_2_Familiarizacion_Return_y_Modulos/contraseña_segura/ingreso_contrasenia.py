def ingreso_contrasenia():
    """Esta funcion sirve para ingresar la contraseña y verificar si es correcta."""
    mensaje = """La constraseña deberá cumplir con los siguientes requisitos:
    Longitud minima: 8
    Cantidad minima de mayusculas: 1
    Cantidad minima de minusculas: 1
    Cantidad minima de caracteres especiales: 1"""
    print(mensaje)
    contrasenia = input("Por favor ingrese la contraseña:\n")
    return contrasenia

if __name__ == "__main__":
    contrasenia = ingreso_contrasenia() #definimos esto para que al llamar la funcion no se ejecute acutomaticamente