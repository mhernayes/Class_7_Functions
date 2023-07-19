#se puede importar la funcion de esta forma:
#from ingreso_producto import ingreso_producto #del archivo ingreso_producto importamos la funcion ingreso_producto
#pero la funcion va sin el "ip."
#o se puede importar directamente el archivo completo

import ingreso_producto as ip

def info_ventas():
    """Esta funcion calcula:
    - La cantidad total de productos
    - El producto de mayor precio
    - El producto con mayor ventas
    - La cantidad total de producto vendidos"""

    lista_producto = ip.ingreso_producto()
    cantidad_total_productos = len(lista_producto) #medidmos la longituda del a lista

    precio_max = 0 #definimos esta variable en 0 para calcular el precio maximo
    producto_precio_max = "" #definimos esta variable vacia para asignarle el valor de del producto del precio maximo
    for producto, datos in lista_producto: #desempaquetamos la lista en producto y datos
        precio = datos['Precio:'] #accedemos a los precios 
        if precio > precio_max: #buscamos el precio mayor y se lo asignamos a producto_precio_max
            precio_max = precio
            producto_precio_max = producto

    ventas_max = 0 #definimos esta variable en 0 para calcular las ventas maximas
    producto_ventas_max = "" #definimos esta variable vacia para asignarle el valor de del producto con mayores ventas
    for producto, datos in lista_producto: #desempaquetamos la lista en producto y datos
        ventas = datos['Ventas:'] #accedemos a las ventas
        if ventas > ventas_max: #buscamos el producto mayor numero de ventas y se lo asignamos a producto_ventas_max
            ventas_max = ventas
            producto_ventas_max = producto



    total_vendidos = 0 #definimos esta variable en 0 para calcular el total prodcutos vendidos
    for producto, datos in lista_producto: #desempaquetamos la lista en producto y datos
        ventas = datos['Ventas:'] #buscamos las ventas y las vamos añadiendo a la variable total_vendidos
        total_vendidos += ventas

    print("La cantidad Total de tipos de Productos vendidos es:", cantidad_total_productos)
    print("El producto con precio máximo es :", producto_precio_max)
    print("El producto con mayores ventas es:", producto_ventas_max)
    print("La cantidad Total de Productos vendidos es:", total_vendidos)
    




