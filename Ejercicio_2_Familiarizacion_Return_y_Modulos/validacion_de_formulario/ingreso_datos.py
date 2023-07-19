def ingreso_nombre():
    nombre = input("Ingrese su nombre:\n")
    nombre_formateado = nombre.title()
    return nombre_formateado

def ingreso_apellido():
    apellido = input("Ingrese su apellido:\n")
    apellido_formateado = apellido.title()
    return apellido_formateado

def ingreso_email():
    email = input("Ingrese su correo electronico:\n")
    email_formateado = email.lower()
    return email_formateado

def ingreso_telefono():
    telefono = input("Ingrese su numero de telefono:\n")
    return telefono

if __name__ == "__main__":
    nombre = ingreso_nombre()
    apellido = ingreso_apellido()
    email = ingreso_email()
    telefono = ingreso_telefono()
