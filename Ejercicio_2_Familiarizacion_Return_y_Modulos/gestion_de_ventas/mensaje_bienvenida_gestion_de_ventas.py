def mensaje_bienvenida():
    "Esta funcion es para dar la bienvenida al programa y para dar el saludo general"
    nombre_programa = "Gestion de Ventas"
    mensaje = """
    ---------------------------------
    Bienvenidos al programa {}
    ---------------------------------
    Este programa sirve para ingresar productos vendidos y mostrar las ventas.
    Una vez ingresados los productos, el programa calculara:
    - La cantidad total de productos
    - El producto de mayor precio
    - El producto con mayor ventas
    - La cantidad total de producto vendidos""".format(nombre_programa)
    print(mensaje)
    