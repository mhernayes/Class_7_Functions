def ingreso_producto():
    """Esta funcion sirve para ingresar el nombre del producto, el precio y la cantidad vendad.
    Si el producto ya esta ingresado, se actualizan los datos."""
    #vamos a estructurar la informacion asi:
    #lista_producto = [[producto1, {"Precio:": XX, "Venta:": XX"}],[producto2, {"Precio:": XX, "Venta:": XX"}]] 
    lista_productos = []
    info_producto = {}
    #colocamos un bucle while True para repetir el ingreso de las notas
    while True:
        #con un try except controlamos el ValueError
        try:
            nombre_producto = input("Por favor ingrese el nombre del producto:\n")
            precio_producto = int(input("Por favor ingrese el precio del producto:\n"))
            cantidad_vendida = int(input("Por favor ingrese el número de ventas del producto ingresado:\n"))
            info_producto = {"Precio:": precio_producto,
                            "Ventas:": cantidad_vendida,
                            }
            #se controla los datos ingresados con un try except     
            opcion = input("¿Desea ingresar otro producto? (s/n): ")
            #con un if verificamos la respuesta ingresada
            if opcion.lower() == 's':
                #agregamos al diccionario 
                #si el producto ya se encontraba ingresado le sumamos la cantidad
                encontrado = False #utilizamos esta variable para recorrer el for hasta encontrar el producto
                for elemento in lista_productos: #recorremos la lista principal lista_productos
                    if elemento[0] == nombre_producto: #buscamos el nombre del producto en nuestra lista
                        #actualizamos el precio y la cantidad vendida si lo encontramos
                        indice_producto = lista_productos.index(elemento)
                        info_producto["Precio:"] = precio_producto
                        info_producto["Ventas:"] = lista_productos[indice_producto][1]["Ventas:"] + cantidad_vendida #unicamente le agregamos cantidad vendida al total
                        lista_productos[indice_producto][1] = info_producto
                        encontrado = True #encontramos el producto en la lista
                    #si el producto no se encontraba ingresado le agregamos la cantidad
                if not encontrado: #encontrado == False
                    sub_lista_productos = [] #definimos una lista vacia
                    #agregamos el producto a mi sub lista de productos
                    sub_lista_productos.append(nombre_producto) #agregamos al producto a mi lista
                    sub_lista_productos.append(info_producto) #agregamos la info del producto a mi lista
                    lista_productos.append(sub_lista_productos) #agregamos la sub lista a la lista principal
            elif opcion.lower() == 'n':
                encontrado = False #utilizamos esta variable para recorrer el for hasta encontrar el producto
                #si el producto ya se encontraba ingresado le sumamos la cantidad
                for elemento in lista_productos: #recorremos la lista principal lista_productos                
                    if elemento[0] == nombre_producto: #buscamos el nombre del producto en nuestra lista
                        #actualizamos el precio y la cantidad vendida si lo encontramos
                        indice_producto = lista_productos.index(elemento)
                        info_producto["Precio:"] = precio_producto
                        info_producto["Ventas:"] = lista_productos[indice_producto][1]["Ventas:"] + cantidad_vendida #unicamente le agregamos cantidad vendida al total
                        lista_productos[indice_producto][1] = info_producto
                        encontrado = True #encontramos el producto en la lista
                        break #salimos del for
                    #si el producto no se encontraba ingresado le agregamos la cantidad
                if not encontrado: #encontrado == False
                    sub_lista_productos = [] #definimos una lista vacia
                    #agregamos el producto a mi sub lista de productos
                    sub_lista_productos.append(nombre_producto) #agregamos al producto a mi lista
                    sub_lista_productos.append(info_producto) #agregamos la info del producto a mi lista
                    lista_productos.append(sub_lista_productos) #agregamos la sub lista a la lista principal
                #salimos del while
                break
            else:
                print("Producto no ingresado. Vuelva a intentarlo.")     
        except ValueError:
            print("Los datos ingresados no son correctos")
    return lista_productos #la variable que se devuelve es lista_productos

#if __name__ == "__main__":
    lista_producto = ingreso_producto() #definimos esto para que al llamar la funcion no se ejecute acutomaticamente