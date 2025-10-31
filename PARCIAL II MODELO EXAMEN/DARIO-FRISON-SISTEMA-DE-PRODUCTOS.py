import csv
import os

NOMBRE_ARCHIVO = 'productos.csv'


def obtener_productos():
    '''
    Lee el archivo CSV y devuelve una lista de productos como diccionarios.
    Si el archivo no existe, lo crea con los encabezados correspondientes.

    Returns:
        list[dict]: Lista de productos con claves 'nombre' y 'precio' (float).
    '''

    # Verificar si el archivo existe; si no, crearlo con encabezados
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open (NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:

            escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'precio'])
            escritor.writeheader()
            return []

    productos = []

    # Leer los productos del archivo CSV
    with open(NOMBRE_ARCHIVO, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        # Agregar cada fila como un diccionario a la lista de productos
        # Convertir el precio a float
        for fila in lector:
            productos.append({'nombre': fila['nombre'], 'precio': float(fila['precio'])})
    return productos

def escribir_producto(producto):
    '''
    Agrega un nuevo producto al archivo CSV.

    Args:
        producto (dict): Diccionario con claves 'nombre' y 'precio'.
    '''

    # Modo 'a' para agregar al final del archivo (sin sobrescribir el contenido existente)
    with open(NOMBRE_ARCHIVO, 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'precio'])
        escritor.writerow(producto)

def existe_producto(nombre):
    '''
    Verifica si un producto con el nombre dado ya existe en el archivo CSV.

    Args:
        nombre (str): Nombre del producto a verificar.
    
    Returns:
        bool: True si el producto existe, False en caso contrario.
    '''
    productos = obtener_productos()

    # Recorrer la lista de productos para buscar coincidencia por nombre
    for producto in productos:
        if producto['nombre'].lower() == nombre.strip().lower():
            return True

    return False


def validar_numero_positivo(valor):
    '''
    Verifica si el valor dado es un número positivo (entero o decimal).

    Args:
        valor (str): Valor a validar.
    
    Returns:
        bool: True si es un número positivo, False en caso contrario.
    '''
    # No puede tener mas de un punto decimal
    if valor.count('.') > 1:
        return False
    
    # Debe estar formado solo por dígitos ignorando un posible punto
    if not valor.replace('.', '').isdigit():
        return False

    return True


def mostrar_productos():
    '''
    Muestra en pantalla la lista de productos guardados en el archivo CSV.
    '''
    print('\nLista de productos:')
    productos = obtener_productos()
    
    print('Nombre   Precio')
    for producto in productos:
        print(f"- {producto['nombre']}: ${producto['precio']}")


def agregar_producto():
    '''
    Solicita al usuario los datos de un nuevo producto y lo agrega al archivo CSV.
    Verifica que el producto no exista previamente y que el precio sea válido.
    '''
    print('\nAgregar nuevo producto:')

    # Solicitar datos y validarlos
    nombre = input('Nombre del producto: ').strip()

    if existe_producto(nombre):
        print(f'El producto "{nombre}" ya existe. No se puede agregar duplicados.')
        return
    
    precio = input('Precio del producto: ').strip()

    if not validar_numero_positivo(precio):
        print('Precio inválido.')
        return
    #  Convertir el precio a float antes de guardarlo
    precio = float(precio)

    escribir_producto({'nombre': nombre, 'precio': precio})
    print(f'Producto "{nombre}" agregado con éxito.')


def guardar_productos(productos):
    '''
    Guarda la lista de productos en el archivo CSV.

    Args:
        productos (list[dict]): Lista de productos a guardar con claves 'nombre' y 'precio'.
    '''

    # Modo 'w' para sobrescribir el archivo con la nueva lista de productos
    with open(NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'precio'])
        escritor.writeheader()
        escritor.writerows(productos)


def editar_producto():
    '''
    Permite al usuario editar el precio de un producto existente.
    Verifica que el producto exista y que el nuevo precio sea válido.
    '''

    productos = obtener_productos()

    # Solicitar y validar el nombre del producto a editar
    nombre = input('Ingrese el nombre del producto a editar: ').strip()

    if not nombre:
        print('El nombre del producto no puede estar vacío.')
        return 

    # Recorrer la lista de productos para encontrar el producto a editar
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            # Solicitar y validar el nuevo precio
            precio = input('Ingrese el nuevo precio: ').strip()

            if not validar_numero_positivo(precio):
                print('Precio inválido.')
                return
            
            # Modificar el precio del producto
            producto['precio'] = float(precio)

            # Escribir los cambios en el archivo CSV
            guardar_productos(productos)
            print(f'Producto "{nombre}" actualizado con éxito.')
            break 
    else:
        #  Se ejecuta si el bucle no encontró el producto
        print(f'El producto "{nombre}" no existe.')



def eliminar_producto():
    '''
    Eliminar un producto del archivo CSV.
    Verifica que el producto exista antes de eliminarlo.
    '''
    # Solicitar y validar el nombre del producto a eliminar
    nombre = input('Ingrese el nombre del producto a eliminar: ').strip()

    if not nombre:
        print('El nombre del producto no puede estar vacío.')
        return
    
    productos = obtener_productos()

    # Crear una nueva lista sin el producto a eliminar
    products_filtrados = []
    for producto in productos:
        if producto['nombre'].lower() != nombre.lower():
            products_filtrados.append(producto)

    # Verificar si se encontró algún producto
    if len(products_filtrados) == len(productos):
        print(f'El producto "{nombre}" no existe.')
        return

    # Guardar los productos filtrados en el archivo CSV
    guardar_productos(products_filtrados)
    print(f'Producto "{nombre}" eliminado con éxito.')


def mostrar_menu():
    '''
    Muestra el menú principal del Sistema
    Permite al usuario seleccionar entre mostrar, agregar, editar o eliminar productos.
    '''

    while True:
        print('\n--- Menú de Gestión de Productos ---')
        print('-'* 40)
        print('1. Mostrar productos ')
        print('2. Agregar producto ')
        print('3. Editar precio de producto ')
        print('4. Eliminar producto ')
        print('5. Salir ')
        print('-'* 40)

        opcion = input('Ingrese una opción (1-5): ').strip()

        match opcion:
            case '1':
                mostrar_productos()
            case '2':
                agregar_producto()
            case '3':
                editar_producto()
            case '4':
                eliminar_producto()
            case '5':
                print('Gracias por usar el sistema. ¡Hasta luego!')
                break
            case _:
                print('Opción inválida. Por favor, elija una opción del 1 al 5.')


# Iniciar el programa mostrando el menú
mostrar_menu()