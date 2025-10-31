import csv
import os

NOMBRE_ARCHIVO = 'productos.csv'


def obtener_productos():

    # Verificar si el archivo existe; si no, crearlo con encabezados
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open (NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:

            escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'precio'])
            escritor.writeheader()
            return []

    # Leer los productos del archivo CSV
    productos = []
    with open(NOMBRE_ARCHIVO, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos.append({'nombre': fila['nombre'], 'precio': float(fila['precio'])})
    return productos

def escribir_producto(producto):
    with open(NOMBRE_ARCHIVO, 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'precio'])
        escritor.writerow(producto)

def existe_producto(nombre):
    productos = obtener_productos()
    
    for producto in productos:
        if producto['nombre'].lower() == nombre.strip().lower():
            return True

    return False


def validar_numero_positivo(valor):
    # Verificar cantidad de puntos
    if valor.count('.') > 1:
        return False
    
    # Verificar si es un número válido
    if not valor.replace('.', '').isdigit():
        return False

    return True


def mostrar_productos():
    print('\nLista de productos:')
    productos = obtener_productos()
    
    print('Nombre   Precio')
    for producto in productos:
        print(f"- {producto['nombre']}: ${producto['precio']}")


def agregar_producto():
    print('\nAgregar nuevo producto:')

    # Solicitar datos del producto
    nombre = input('Nombre del producto: ').strip()
    if existe_producto(nombre):
        print(f'El producto "{nombre}" ya existe. No se puede agregar duplicados.')
        return
    
    precio = input('Precio del producto: ').strip()
    if not validar_numero_positivo(precio):
        print('Precio inválido.')
        return
    precio = float(precio)

    # Agregar el producto al archivo CSV
    escribir_producto({'nombre': nombre, 'precio': precio})
    print(f'Producto "{nombre}" agregado con éxito.')


def guardar_productos(productos):
    with open(NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'precio'])
        escritor.writeheader()
        escritor.writerows(productos)


def editar_producto():
    productos = obtener_productos()

    nombre = input('Ingrese el nombre del producto a editar: ').strip()

    if not nombre:
        print('El nombre del producto no puede estar vacío.')
        return 

    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
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
        print(f'El producto "{nombre}" no existe.')

def eliminar_producto():
    # Solicitar y validar el nombre del producto a eliminar
    nombre = input('Ingrese el nombre del producto a eliminar: ').strip()

    if not nombre:
        print('El nombre del producto no puede estar vacío.')
        return
    
    #  Obtener la lista de productos y filtrar el que se va a eliminar
    productos = obtener_productos()
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
                print('Gracias por usar el sistema. :)')
                break
            case _:
                print('Opción inválida. Por favor, elija una opción del 1 al 5.')

mostrar_menu()