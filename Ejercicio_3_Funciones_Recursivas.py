""""
Ejercicio 3.1
FACTORIAL
Implementa una función recursiva llamada factorial que calcule el factorial
de un número entero positivo. El factorial de un número n se define como el 
producto de todos los números enteros positivos desde 1 hasta n.
(El factorial de 0 y de 1 es igual a 1)
"""
def factorial(i):
    "Calculo de factorial."
    if i == 0 or i == 1:
        return 1
    else:   
        return i * factorial(i-1)
print("----- CALCULO DE FACTORIAL -----")
numero = int(input("Ingrese un numero:\n"))
resultado = factorial(numero)
print("El resultado es:", resultado)

"""
Ejercicio 3.2
POTENCIA
Implementa una función recursiva llamada potencia que calcule el resultado de 
elevar un número a una potencia dada. Puedes asumir que tanto el número como la 
potencia son enteros no negativos.
"""

def potencia(base, exponente):
    "Calculo de potencia."
    if exponente == 0:
        return 1
    else:   
        return base * potencia(base, exponente - 1)
    
print("----- CALCULO DE POTENCIA -----")
base = int(input("Ingrese un numero base:\n"))
exponente = int(input("Ingrese un numero exponente:\n"))
resultado = potencia(base, exponente)
print("El resultado del calculo de la potencia es:", resultado)

"""
Ejercicio 3.3
SUMA ELEMENTOS DE UNA LISTA
Crea una función recursiva llamada suma_lista que calcule la suma de todos los 
elementos de una lista de enteros. Puedes asumir que la lista no está vacía.
"""
def suma_lista(lista):
    "Suma de elementos de una lista."
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + suma_lista(lista[1:])

print("----- SUMA ELEMENTOS DE UNA LISTA -----")
lista = [1,2,3,4,5]
resultado = suma_lista(lista)
print("La suma de los numeros de la lista es:", resultado)

"""
Ejercicio 3.4
NUMERO TRIANGULAR
Crea una función recursiva llamada numero_triangular que calcule el n-ésimo 
número triangular. Un número triangular se obtiene al sumar todos los números 
naturales desde 1 hasta n.
"""

def numero_triangular(numero):
    "Calculo de numero triangular."
    if numero == 1:
        return 1
    else:
        return numero + numero_triangular(numero - 1)
    
print("----- CALCULO DE NUMERO TRIANGULAR -----")
numero = int(input("Ingrese un numero:\n"))
resultado = numero_triangular(numero)
print("El resultado del numero triangular es:", resultado)