import re #importamos la biblioteca re
import ingreso_contrasenia as ic #importamos el archivo ingreso_contrasenia.py

def validar_contrasenia(contrasenia): #definimos la funcion valida_contrasenia y le pasamos como parametro la contraseña del otro archivo
    contrasenia_validada = False
    while contrasenia_validada == False: #con un bucle preguntamos que se ingrese la contraseña hasta que la misma sea valida
        contrasenia = ic.ingreso_contrasenia() #asignamos a la variable contrasenia la funcion del arhicov ingreso_contrasenia.py que solicita el ingreso
        if len(contrasenia) < 8: #Verificar longitud mínima
            contrasenia_validada = False
            
        if not re.search(r'[A-Z]', contrasenia): #Verificar cantidad mínima de mayúsculas
            contrasenia_validada = False
        
        if not re.search(r'[a-z]', contrasenia): #Verificar cantidad mínima de minúsculas
            contrasenia_validada = False
        
        if not re.search(r'[\W_]', contrasenia):# Verificar cantidad mínima de caracteres especiales
            contrasenia_validada = False

        else: #si se cumplen todas las condiones anteriores la contraseña es valida
            contrasenia_validada = True
        
        if contrasenia_validada == False: #si la contraseña es invalida se imprime por pantalla
            print("La contraseña no cumple con los requisitos.")
        else:
            contrasenia_validada == True #si la contraseña es valida se imprime por pantalla
            print("CONTRASEÑA VALIDA.")
            break

if __name__ == "__main__":
    contrasenia = ic.ingreso_contrasenia()
    validar_contrasenia(contrasenia) #definimos esto para que al llamar la funcion no se ejecute acutomaticamente