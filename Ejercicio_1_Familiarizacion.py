"""
1. Define una función llamada "saludar" que tome un parámetro "nombre" y muestre un saludo 
personalizado.
2. Crea una función llamada "suma" que tome dos parámetros "a" y "b" e imprima la suma de ambos.
3. Escribe una función llamada "calcular_area_rectangulo" que tome dos parámetros "base" y 
"altura" y calcule el área de un rectángulo.
4. Define una función llamada "imprimir_lista" que tome una lista como parámetro y la imprima 
en la consola.
5. Crea una función llamada "es_par" que tome un número como parámetro e imprima True si 
es par, o False si es impar.
6. Escribe una función llamada "concatenar_strings" que tome dos parámetros "cadena1" y 
“cadena2" e imprima la concatenación de ambas cadenas.
7. Define una función llamada "obtener_maximo" que tome una lista de números como parámetro 
y devuelva el número máximo de la lista.
8. Crea una función llamada "convertir_fahrenheit_a_celsius" que tome un parámetro "fahrenheit" 
y devuelva su equivalente en grados Celsius.
9. Escribe una función llamada "calcular_edad" que tome dos parámetros: "año_actual" y 
"año_nacimiento" y calcule la edad de una persona.
10. Define una función llamada "es_divisible" que tome dos parámetros "num" y "divisor" 
e imprima True si "num" es divisible por "divisor", o False si no lo es.
11. Crea una función llamada "mostrar_info_persona" que tome tres argumentos de palabra 
clave: "nombre", "edad" y "ciudad". La función debe imprimir en la consola la información 
de una persona en un formato legible.
12. Escribe una función llamada "calcular_promedio" que tome una lista de números como parámetro 
y calcule el promedio de esos números. Si no se proporciona una lista, debe usar una lista vacía por defecto.
13. Crea una función llamada "calcular_potencia" que tome dos parámetros "base" y "exponente", 
y calcule la potencia de la base elevada al exponente. Utiliza 2 como valor por defecto para el exponente.
14. Define una función llamada "imprimir_info_alumno" que tome un argumento posicional “nombre”
(y sin valor por defecto) y varios argumentos de palabra clave: "edad", "curso" y “promedio" (puedes ponerles 
como valor por defecto None). La función debe imprimir la información del alumno en un formato legible.
"""

#1. Define una función llamada "saludar" que tome un parámetro "nombre" y muestre un saludo 
# personalizado.
print("---------- Ejercicio 1 ---------")

def saludar(nombre):
    "A la funcion se le pasa un parametro nombre y muestra un saludo"
    print("Esta funcion imprime un saludo")
    print("Hola", nombre)

saludar(nombre = "Martin")

#2. Crea una función llamada "suma" que tome dos parámetros "a" y "b" e imprima la suma de ambos.
print("---------- Ejercicio 2 ---------")
def suma(a, b):
    "Esta funcion realiza la suma de 2 valores"
    print("Esta funcion realiza la suma de 2 valores")
    suma = a + b
    print("La suma de los valores es", suma)

def ingreso_valores_suma():
    "Esta funcion es para ingresar los valores"
    a = int(input("Ingrese el valor A:\n"))
    b = int(input("Ingrese el valor B:\n"))
    return (a,b)
#llamamos a la funcion ingreso_valores_suma y guardamos lo que devuelve la funcion en 2 variables
a, b = ingreso_valores_suma()

#llamamos a la funcion suma para que realice la suma
suma(a, b)

#3. Escribe una función llamada "calcular_area_rectangulo" que tome dos parámetros "base" y 
#"altura" y calcule el área de un rectángulo.
print("---------- Ejercicio 3 ---------")
def calcular_area_rectangulo(a, b):
    "Esta funcion realiza el caluclo del area de un rectangulo"
    print("Esta funcion calcula el area de un rectangulo")
    area = a * b
    print("El area del rectangulo es:" , area)

def ingreso_valores_lados():
    "Esta funcion es para ingresar los lados del rectangulo"
    a = int(input("Ingrese el lado A:\n"))
    b = int(input("Ingrese el lado B:\n"))
    return (a,b)
#llamamos a la funcion ingreso_valores_lados y guardamos lo que devuelve la funcion en 2 variables
a, b = ingreso_valores_lados()

#llamamos a la funcion suma para que realice la suma
calcular_area_rectangulo(a, b)

#4. Define una función llamada "imprimir_lista" que tome una lista como parámetro y la imprima 
# en la consola.

print("---------- Ejercicio 4 ---------")
def imprimir_lista(lista):
    "Esta funcion es para imprimir la lista ingresada"
    print("Esta funcion es para imprimir la lista")
    print("La lista ingresada de numeros es:")
    #Convierte cada elemento de la lista a cadena
    elementos_cadena = [str(elemento) for elemento in lista]
    #Une los elementos de la lista separados por coma y espacio
    lista_sin_corchetes = ", ".join(elementos_cadena)  
    print(lista_sin_corchetes)

def ingreso_valores_lista():
    "Esta funcion es para ingresar los valores"
    #creamos una lista vacia
    lista = []
    #creamos un bucle que sirve para llenar la lista con los valores
    ingresar = True
    #con un while seguimos preguntando si queremos ingresar ingresar mas valores
    while ingresar == True:
        valor = int(input("Ingrese un numero:\n"))
        lista.append(valor)
        pregunta = input("Desea ingresar otro valor? s/n\n")
        if pregunta == "s":
            ingresar = True
        elif pregunta == "n":
            ingresar = False
        else:
            print("Respuesta incorrecta, ingrese nuevamente el numero y luego ingrese 's' o 'n'")
            ingresar = True
    return(lista)

#llamamos a la funcion ingreso_valores_lista y guardamos lo que devuelve la funcion en 1 variable
lista = ingreso_valores_lista()

#llamamos a la funcion imprimir_lista para imrpimir la lista
imprimir_lista(lista)

#5. Crea una función llamada "es_par" que tome un número como parámetro e imprima True si 
# es par, o False si es impar.
print("---------- Ejercicio 5 ---------")
def es_par(a):
    "Esta funcion verifica si un numero es par"
    print("Esta funcion verifica si un numero es par")
    if a % 2 == 0:
        print("El numero ingresado es par")
    else:
        print("El numero ingresado es impar")

def ingreso_valor_par():
    "Esta funcion es para ingresar los valores"
    a = int(input("Ingrese el valor A:\n"))
    return a
#llamamos a la funcion ingreso_valores_par y guardamos lo que devuelve la funcion en 1 variable
a = ingreso_valor_par()

#llamamos a la funcion es_par para que verifique si el numero ingresado es par
es_par(a)

#6. Escribe una función llamada "concatenar_strings" que tome dos parámetros "cadena1" y 
#“cadena2" e imprima la concatenación de ambas cadenas.
print("---------- Ejercicio 6 ---------")
def concatenar_string(cadena_1, cadena_2):
    "Esta funcion concatena 2 cadenas de texto"
    print("Esta funcion concatena 2 cadenas de texto")
    cadena_3 = cadena_1 + " " + cadena_2
    print("El texto concatenado es:", cadena_3)

def ingreso_valores_cadena():
    "Esta funcion es para ingresar los valores"
    cadena_1 = input("Ingrese el texto 1:\n")
    cadena_2 = input("Ingrese el texto 2:\n")
    return (cadena_1, cadena_2)
#llamamos a la funcion ingreso_valores_cadena y guardamos lo que devuelve la funcion en 2 variables
cadena_1, cadena_2 = ingreso_valores_cadena()

#llamamos a la funcion es_par para que verifique si el numero ingresado es par
concatenar_string(cadena_1, cadena_2)

#7. Define una función llamada "obtener_maximo" que tome una lista de números como parámetro 
#y devuelva el número máximo de la lista.
print("---------- Ejercicio 7 ---------")
def obtener_maximo(lista):
    "Esta funcion es para obtener el numero maximo de la lista ingresada"
    print("Esta funcion es para obtener el numero maximo de la lista ingresada")
    print("La lista ingresada de numeros es:")
    #Convierte cada elemento de la lista a cadena
    elementos_cadena = [str(elemento) for elemento in lista]
    #Une los elementos de la lista separados por coma y espacio
    lista_sin_corchetes = ", ".join(elementos_cadena)  
    print(lista_sin_corchetes)
    maximo = max(lista)
    print("El numero maximo es:", maximo)

def ingreso_valores_lista():
    "Esta funcion es para ingresar los valores"
    #creamos una lista vacia
    lista = []
    #creamos un bucle que sirve para llenar la lista con los valores
    ingresar = True
    #con un while seguimos preguntando si queremos ingresar ingresar mas valores
    while ingresar == True:
        valor = int(input("Ingrese un numero:\n"))
        lista.append(valor)
        pregunta = input("Desea ingresar otro valor? s/n\n")
        if pregunta == "s":
            ingresar = True
        elif pregunta == "n":
            ingresar = False
        else:
            print("Respuesta incorrecta, ingrese nuevamente el numero y luego ingrese 's' o 'n'")
            ingresar = True
    return(lista)

#llamamos a la funcion ingreso_valores_lista y guardamos lo que devuelve la funcion en 1 variable
lista = ingreso_valores_lista()

#llamamos a la funcion obtener_maximo para que verifique cual es el numero maximo
obtener_maximo(lista)

#8. Crea una función llamada "convertir_fahrenheit_a_celsius" que tome un parámetro "fahrenheit" 
#y devuelva su equivalente en grados Celsius.
print("---------- Ejercicio 8 ---------")
def convertir_fahrenheit_a_celsius(a):
    "Esta funcion es para convertir el valor de la temperatura de fahrenheit a a celsius"
    print("Esta funcion es para convertir el valor de la temperatura de fahrenheit a a celsius")
    #ºC = (ºF-32) ÷ 1.8
    temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32
    print("La temperatura en grados Fahrenheit es de:", temperatura_fahrenheit)

def ingreso_valor_temperatura():
    "Esta funcion es para ingresar el valor de la temperatura"
    temperatura_celsius = int(input("Ingrese el valor de la temperatura:\n"))
    return temperatura_celsius
#llamamos a la funcion ingreso_valor_temperatura y guardamos lo que devuelve la funcion en 1 variable
temperatura_celsius = ingreso_valor_temperatura()

#llamamos a la funcion convertir_fahrenheit_a_celsius para que convierta la temperatura
convertir_fahrenheit_a_celsius(temperatura_celsius)

#9. Escribe una función llamada "calcular_edad" que tome dos parámetros: "año_actual" y 
#"año_nacimiento" y calcule la edad de una persona.
from datetime import datetime as dt
print("---------- Ejercicio 9 ---------")
def calcular_edad(a):
    "Esta funcion ees para calcular la edad"
    print("Esta funcion es para calcular la edad")
    #ºC = (ºF-32) ÷ 1.8
    fecha_actual = dt.today()
    fecha_actual_formateada = fecha_actual.strftime("%d/%m/%Y")
    edad = fecha_actual.year - fecha_nacimiento_formateada.year
    print("La edad de acuerdo al a fecha actual:", fecha_actual_formateada, "es:", edad)

def ingreso_valor_fecha_nacimiento():
    "Esta funcion es para ingresar la fecha de nacimiento"
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (dd/mm/aaaa):\n")
    fecha_nacimiento_formateada = dt.strptime(fecha_nacimiento, "%d/%m/%Y").date()
    return fecha_nacimiento_formateada

#llamamos a la funcion ingreso_valor_fecha_nacimiento y guardamos lo que devuelve la funcion en 1 variable
fecha_nacimiento_formateada = ingreso_valor_fecha_nacimiento()

#llamamos a la funcion calcular_edad para verificar que edad tiene la persona
calcular_edad(fecha_nacimiento_formateada)

#10. Define una función llamada "es_divisible" que tome dos parámetros "num" y "divisor" 
#e imprima True si "num" es divisible por "divisor", o False si no lo es.
print("---------- Ejercicio 10 ---------")
def es_divisible(num, divisor):
    "Esta funcion verifica si un numero es divisible por otro"
    print("Esta funcion verifica si un numero es divisible por otro")
    if num % divisor == 0:
        print("El numero ingresado es divisible por el divisor")
    else:
        print("El numero ingresado no es divisible por el divisor")

def ingreso_valores_divisible():
    "Esta funcion es para ingresar los valores"
    num = int(input("Ingrese un numero:\n"))
    divisor = int(input("Ingrese un divisor:\n"))
    return (num, divisor)

#llamamos a la funcion ingreso_valores_divisible y guardamos lo que devuelve la funcion en 2 variables
num, divisor = ingreso_valores_divisible()

#llamamos a la funcion suma para que realice la suma
es_divisible(num, divisor)

#11. Crea una función llamada "mostrar_info_persona" que tome tres argumentos de palabra 
# clave: "nombre", "edad" y "ciudad". La función debe imprimir en la consola la información 
# de una persona en un formato legible.
print("---------- Ejercicio 11 ---------")
def mostrar_info_persona(nombre, edad, ciudad):
    "Esta funcion mostrar la informacion de la persona"
    print("Esta funcion es para mostrar la informacion de la persona")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Ciudad:", ciudad)

def ingreso_valores_persona():
    "Esta funcion es para ingresar los valores"
    nombre = input("Ingrese su nombre:\n")
    edad = int(input("Ingrese su edad:\n"))
    ciudad = input("Ingrese su ciudad:\n")
    return (nombre, edad, ciudad)

#llamamos a la funcion ingreso_valores_alumno y guardamos lo que devuelve la funcion en 3 variables
nombre, edad, ciudad = ingreso_valores_persona()

#llamamos a la funcion mostrar_info_persona para que realice la suma
mostrar_info_persona(nombre, edad, ciudad)

#12. Escribe una función llamada "calcular_promedio" que tome una lista de números como parámetro
#y calcule el promedio de esos números. Si no se proporciona una lista, debe usar una lista vacía por defecto.
print("---------- Ejercicio 7 ---------")
def calcular_promedio(lista):
    "Esta funcion es para obtener promedio de los numeros de la lista ingresada"
    print("Esta funcion es para obtener promedio de los numeros de la lista ingresada")
    print("La lista ingresada de numeros es:")
    #Convierte cada elemento de la lista a cadena
    elementos_cadena = [str(elemento) for elemento in lista]
    #Une los elementos de la lista separados por coma y espacio
    lista_sin_corchetes = ", ".join(elementos_cadena)  
    print(lista_sin_corchetes)
    suma = 0
    for elemento in lista:
        suma += elemento
    promedio = suma / len(lista)
    print("El numero maximo es:", promedio)

def ingreso_valores_lista():
    "Esta funcion es para ingresar los valores"
    #creamos una lista vacia
    lista = []
    #creamos un bucle que sirve para llenar la lista con los valores
    ingresar = True
    #con un while seguimos preguntando si queremos ingresar ingresar mas valores
    while ingresar == True:
        valor = int(input("Ingrese un numero:\n"))
        lista.append(valor)
        pregunta = input("Desea ingresar otro valor? s/n\n")
        if pregunta == "s":
            ingresar = True
        elif pregunta == "n":
            ingresar = False
        else:
            print("Respuesta incorrecta, ingrese nuevamente el numero y luego ingrese 's' o 'n'")
            ingresar = True
    return(lista)

#llamamos a la funcion ingreso_valores_lista y guardamos lo que devuelve la funcion en 1 variable
lista = ingreso_valores_lista()

#llamamos a la funcion calcular_promedio para que calcule el promedio de los numeros de la lista
calcular_promedio(lista)

#13. Crea una función llamada "calcular_potencia" que tome dos parámetros "base" y "exponente", 
#y calcule la potencia de la base elevada al exponente. Utiliza 2 como valor por defecto para el exponente.
print("---------- Ejercicio 13 ---------")
def calcular_potencia(base, exponente):
    "Esta funcion es para calcular la potencia"
    print("Esta funcion es para calcular la potencia")
    potencia = base ** exponente
    print("El resultado de la potencia es:", potencia)

def ingreso_valores_potencia():
    "Esta funcion es para ingresar los valores"
    base = int(input("Ingrese el valor la base:\n"))
    exponente = int(input("Ingrese el valor del exponente:\n"))
    return (base,exponente)
#llamamos a la funcion ingreso_valores_potencia y guardamos lo que devuelve la funcion en 2 variables
base, exponente = ingreso_valores_potencia()

#llamamos a la funcion suma para que realice el caluclo de la potencia
calcular_potencia(base, exponente)

#14. Define una función llamada "imprimir_info_alumno" que tome un argumento posicional “nombre”
#(y sin valor por defecto) y varios argumentos de palabra clave: "edad", "curso" y “promedio" (puedes ponerles 
#como valor por defecto None). La función debe imprimir la información del alumno en un formato legible.
#14. Define una función llamada "imprimir_info_alumno" que tome un argumento posicional “nombre”
#(y sin valor por defecto) y varios argumentos de palabra clave: "edad", "curso" y “promedio" (puedes ponerles 
#como valor por defecto None). La función debe imprimir la información del alumno en un formato legible.
print("---------- Ejercicio 14 ---------")
def imprimir_info_alumno(nombre, edad, curso, promedio):
    "Esta funcion mostrar la informacion del alumno"
    print("Esta funcion es para mostrar la informacion del alumno")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Curso:", curso)
    print("Promedio:", promedio)

def ingreso_valores_alumno():
    "Esta funcion es para ingresar los valores"
    nombre = input("Ingrese su nombre:\n")
    edad = int(input("Ingrese su edad:\n"))
    curso = input("Ingrese su curso:\n")
    promedio = int(input("Ingrese su promedio:\n"))
    return (nombre, edad, curso, promedio)

#llamamos a la funcion ingreso_valores_alumno y guardamos lo que devuelve la funcion en 4 variables
nombre, edad, curso, promedio = ingreso_valores_alumno()

#llamamos a la funcion imprimir_info_alumnos para que imprima la informacion del alumno
imprimir_info_alumno(nombre, edad, curso, promedio)