
from ingreso_datos import ingreso_nombre, ingreso_apellido, ingreso_email, ingreso_telefono

def validacion_datos():
    datos = {} #definimos un diccionario vacio
    dato_ingresado = False #seteamos esta varible para el bucle

    while dato_ingresado == False:
        nombre = ingreso_nombre() #solicimamos el ingreso del nombre llamando a la funcion
        if len(nombre) >= 3: #verificamos el nombre
            datos["nombre"] = nombre #agregamos el dato al diccionario datos
            dato_ingresado = True #salimos del bucle
        else: 
            print("Nombre invalido. Debe contener por lo menos 3 caracteres")

    dato_ingresado = False #seteamos esta varible para el bucle
    while dato_ingresado == False:
        apellido = ingreso_apellido() #solicimamos el ingreso del apellido llamando a la funcion
        if len(apellido) >= 3: #verificamos el apellido
            datos["apellido"] = apellido
            dato_ingresado = True #salimos del bucle
        else: 
            print("Apellido invalido. Debe contener por lo menos 3 caracteres")

    dato_ingresado = False #seteamos esta varible para el bucle
    while dato_ingresado == False:
        telefono = ingreso_telefono() #solicimamos el ingreso del telefono llamando a la funcion
        if len(telefono) == 9: #verificamos el telefono
            datos["telefono"] = telefono
            dato_ingresado = True #salimos del bucle
        else: 
            print("Telefono invalido. Debe contener 9 caracteres.")

    dato_ingresado = False #seteamos esta varible para el bucle
    while dato_ingresado == False:
        email = ingreso_email() #solicimamos el ingreso del email llamando a la funcion
        if "@" in email and "." in email: #verificamos el mail
            datos["email"] = email
            dato_ingresado = True #salimos del bucle

        else: 
            print("Mail invalido. Debe contener '@' y '.'")
    return datos

if __name__ == "__main__":
    datos = validacion_datos()