import csv
import os

NOMBRE_ARCHIVO = 'productos.csv'


def obtener_productos():

    if not os.path.exists(NOMBRE_ARCHIVO):
        with open (NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:

            escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'precio'])
            escritor.writeheader()
            return []


    productos = []

    with open(NOMBRE_ARCHIVO, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos.append({'nombre': fila['nombre'], 'precio': float(fila['precio'])})
    return productos


def mostrar_productos():
    print('\nLista de productos:')
    productos = obtener_productos()
    
    print('Nombre   Precio')
    for producto in productos:
        print(f"- {producto['nombre']}: ${producto['precio']}")


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
                print('Agregar producto')
            case '3':
                print('Editar precio de producto')
            case '4':
                print('Eliminar producto')
            case '5':
                print('Gracias por usar el sistema. :)')
                break
            case _:
                print('Opción inválida. Por favor, elija una opción del 1 al 5.')

mostrar_menu()