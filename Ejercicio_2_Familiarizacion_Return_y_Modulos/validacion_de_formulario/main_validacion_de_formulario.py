"""
VALIDACIÓN DE FORMULARIO
Crea un programa que valide un formulario de registro. Crea una función
llamada validar_formulario que reciba diferentes campos de un formulario
(nombre, correo electrónico y número de teléfono) y verifique si los valores
ingresados cumplen con los requisitos especificados, siendo estos:
1. Que el nombre tenga una longitud minima de 3 caracteres
2. Que el teléfono este conformado por dígitos y tenga una longitud de 9
caracteres
3. Que el email contenga un “@“ y un “.”
"""

import mensaje_bienvenida_validacion_de_formulario as mb #importamos el archivo de mensaje 
import impresion_datos as impd #importamos el archivo de impresion de datos

mb.mensaje_bienvenida() #llamamos a la funcion que imprime el mensaje de bienvenida
impd.impresion_datos() # llamamos a la funcion que valida los datos ingresados
