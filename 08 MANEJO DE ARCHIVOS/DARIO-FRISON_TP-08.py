# TP 8 - Manejo de Archivos - Tecnicatura Universitaria en Programación
# Alumno: Dario Frison

# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

def ejercicio_1():
    # Crear archivo con tres productos iniciales
    with open("productos.txt", "w") as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,350.0,15\n")
        archivo.write("Mochila,2500.0,8\n")
    
    print("Archivo 'productos.txt' creado exitosamente con 3 productos.")
    print()


# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30

def ejercicio_2():
    # Abrir y leer el archivo
    with open("productos.txt", "r") as archivo:
        lineas = archivo.readlines()
    
    print("Productos en el archivo:")
    
    for linea in lineas:
        linea = linea.strip()
        if linea:  # Verificar que la línea no esté vacía
            datos = linea.split(",")
            nombre = datos[0]
            precio = datos[1]
            cantidad = datos[2]
            
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
    
    print()


# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

def ejercicio_3():
    # Leer y mostrar productos existentes
    print("Productos actuales:")
    
    with open("productos.txt", "r") as archivo:
        lineas = archivo.readlines()
    
    for linea in lineas:
        linea = linea.strip()
        if linea:
            datos = linea.split(",")
            nombre = datos[0]
            precio = datos[1]
            cantidad = datos[2]
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
    
    print("\n" + "-" * 50)
    print("Agregar nuevo producto:")
    print("-" * 50)
    
    # Solicitar datos del nuevo producto
    nombre = input("Ingrese el nombre del producto: ")
    
    while True:
        entrada_precio = input("Ingrese el precio: ")
        if entrada_precio.replace('.', '', 1).isdigit():
            precio = entrada_precio
            break
        else:
            print("** Error: Ingrese un precio válido **")
    
    while True:
        entrada_cantidad = input("Ingrese la cantidad: ")
        if entrada_cantidad.isdigit() and int(entrada_cantidad) >= 0:
            cantidad = entrada_cantidad
            break
        else:
            print("** Error: La cantidad debe ser un número entero no negativo **")
    
    # Agregar el nuevo producto al archivo (modo append)
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    
    print(f"\nProducto '{nombre}' agregado exitosamente al archivo.")
    print()


# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

def ejercicio_4():
    productos = []
    
    # Leer archivo y cargar en lista de diccionarios
    with open("productos.txt", "r") as archivo:
        lineas = archivo.readlines()
    
    for linea in lineas:
        linea = linea.strip()
        if linea:
            datos = linea.split(",")
            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])
            }
            productos.append(producto)
    
    print("Productos cargados en lista de diccionarios:")
    print("-" * 50)
    
    for producto in productos:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
    
    print(f"\nTotal de productos cargados: {len(productos)}")
    print()


# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

def ejercicio_5():
    productos = []
    
    with open("productos.txt", "r") as archivo:
        lineas = archivo.readlines()
    
    for linea in lineas:
        linea = linea.strip()
        if linea:
            datos = linea.split(",")
            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])
            }
            productos.append(producto)
    
    print("Productos disponibles:")
    print("-" * 50)
    for producto in productos:
        print(f"  - {producto['nombre']}")
    print("\n" + "-" * 50)
    
    # Buscar producto
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    
    # Recorrer la lista buscando el producto
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print("\n¡Producto encontrado!")
            print("-" * 50)
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"\n** El producto '{nombre_buscar}' no se encuentra en el archivo **")
    
    print()


# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

def ejercicio_6():
    productos = []
    
    with open("productos.txt", "r") as archivo:
        lineas = archivo.readlines()
    
    for linea in lineas:
        linea = linea.strip()
        if linea:
            datos = linea.split(",")
            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])
            }
            productos.append(producto)
    
    print("Productos actuales:")
    print("-" * 50)
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
        
    print("\n" + "-" * 50)
    print("Menú de opciones:")
    print("1. Modificar precio de un producto")
    print("2. Modificar cantidad de un producto")
    print("3. Agregar nuevo producto")
    print("4. Guardar y salir")
    print("-" * 50)
    
    continuar = True
    while continuar:
        opcion = input("\nSeleccione una opción: ")
        
        match opcion:
            case "1":
                # Modificar precio
                nombre = input("Ingrese el nombre del producto: ")
                
                encontrado = False
                for producto in productos:
                    if producto["nombre"].lower() == nombre.lower():
                        print(f"Precio actual: ${producto['precio']}")
                        
                        while True:
                            entrada_precio = input("Ingrese el nuevo precio: ")
                            if entrada_precio.replace('.', '', 1).isdigit():
                                producto["precio"] = float(entrada_precio)
                                print(f"Precio actualizado a ${producto['precio']}")
                                encontrado = True
                                break
                            else:
                                print("** Error: Ingrese un precio válido **")
                        break
                
                if not encontrado:
                    print(f"** Error: Producto '{nombre}' no encontrado **")
            
            case "2":
                # Modificar cantidad
                nombre = input("Ingrese el nombre del producto: ")
                
                encontrado = False
                for producto in productos:
                    if producto["nombre"].lower() == nombre.lower():
                        print(f"Cantidad actual: {producto['cantidad']}")
                        
                        while True:
                            entrada_cantidad = input("Ingrese la nueva cantidad: ")
                            if entrada_cantidad.isdigit() and int(entrada_cantidad) >= 0:
                                producto["cantidad"] = int(entrada_cantidad)
                                print(f"Cantidad actualizada a {producto['cantidad']}")
                                encontrado = True
                                break
                            else:
                                print("** Error: La cantidad debe ser un número entero no negativo **")
                        break
                
                if not encontrado:
                    print(f"** Error: Producto '{nombre}' no encontrado **")
            
            case "3":
                # Agregar nuevo producto
                nombre = input("Ingrese el nombre del nuevo producto: ")
                
                # Verificar si el producto ya existe
                existe = False
                for producto in productos:
                    if producto["nombre"].lower() == nombre.lower():
                        existe = True
                        print(f"** Error: El producto '{nombre}' ya existe en la lista **")
                        print(f"Precio actual: ${producto['precio']} | Cantidad actual: {producto['cantidad']}")
                        print("Use la opción 1 o 2 para modificar un producto existente.")
                        break
                
                # Si no existe, solicitar datos y agregarlo
                if not existe:
                    while True:
                        entrada_precio = input("Ingrese el precio: ")
                        if entrada_precio.replace('.', '', 1).isdigit():
                            precio = float(entrada_precio)
                            break
                        else:
                            print("** Error: Ingrese un precio válido **")
                    
                    while True:
                        entrada_cantidad = input("Ingrese la cantidad: ")
                        if entrada_cantidad.isdigit() and int(entrada_cantidad) >= 0:
                            cantidad = int(entrada_cantidad)
                            break
                        else:
                            print("** Error: La cantidad debe ser un número entero no negativo **")
                    
                    nuevo_producto = {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    }
                    productos.append(nuevo_producto)
                    print(f"Producto '{nombre}' agregado a la lista.")
            
            case "4":
                # Guardar y salir
                continuar = False
            
            case _:
                print("** Opción no válida **")
    
    # Sobrescribir el archivo con todos los productos actualizados
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    
    print("\nArchivo 'productos.txt' actualizado exitosamente.")
    print("\nProductos finales guardados:")
    print("-" * 50)
    for producto in productos:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
    
    print()


# Programa principal
def main():
    # Ejercicio 1
    ejercicio_1()
    # Ejercicio 2
    ejercicio_2()
    # # Ejercicio 3
    ejercicio_3()
    # # Ejercicio 4
    ejercicio_4()
    # # Ejercicio 5
    ejercicio_5()
    # # Ejercicio 6
    ejercicio_6()


main()
