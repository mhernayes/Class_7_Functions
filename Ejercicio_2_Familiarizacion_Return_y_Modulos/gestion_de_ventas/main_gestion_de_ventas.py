"""
GESTIÓN DE VENTAS
Crea un programa que permita gestionar las ventas de una tienda. Utiliza una
estructura de datos adecuada para almacenar la información de las ventas
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para
agregar el producto vendido con su precio y otro para mostrar las ventas de
productos con sus respectivos precios.
(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”:
precio1}, {“Producto”: producto2, “Precio”: precio2}…])
"""

import mensaje_bienvenida_gestion_de_ventas as mb
import info_ventas as iv

mb.mensaje_bienvenida() #llamamos a la funcion mensaje_bienvenida
iv.info_ventas() #llamamos a la funcion info_ventas que calcula todo

