import csv
import os

NOMBRE_ARCHIVO = 'catalogo.csv'


def obtener_libros():
    '''
    Lee el archivo CSV y devuelve una lista de libros como diccionarios.
    Si el archivo no existe, lo crea con los encabezados correspondientes.

    Returns:
        list[dict]: Lista de libros con claves 'TITULO' y 'CANTIDAD' (int).
    '''

    # Verificar si el archivo existe; si no, crearlo con encabezados
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:

            escritor = csv.DictWriter(archivo, fieldnames=['TITULO', 'CANTIDAD'])
            escritor.writeheader()
            return []

    libros = []

    # Leer los libros del archivo CSV
    with open(NOMBRE_ARCHIVO, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        # Agregar cada fila como un diccionario a la lista de libros
        # Convertir la cantidad a int
        for fila in lector:
            libros.append({'TITULO': fila['TITULO'], 'CANTIDAD': int(fila['CANTIDAD'])})
    return libros


def agregar_libro(libro):
    '''
    Agrega un nuevo libro al archivo CSV.

    Args:
        libro (dict): Diccionario con claves 'TITULO' y 'CANTIDAD'.
    '''

    # Modo 'a' para agregar al final del archivo (sin sobrescribir el contenido existente)
    with open(NOMBRE_ARCHIVO, 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['TITULO', 'CANTIDAD'])
        escritor.writerow(libro)


def existe_libro(titulo):
    '''
    Verifica si un libro con el titulo dado ya existe en el archivo CSV.

    Args:
        titulo (str): Titulo del libro a verificar.

    Returns:
        bool: True si el libro existe, False en caso contrario.
    '''
    libros = obtener_libros()

    # Recorrer la lista de libros para buscar coincidencia por título
    for libro in libros:
        if libro['TITULO'].lower() == titulo.strip().lower():
            return True

    return False


def validar_numero_entero_no_negativo(valor):
    '''
    Verifica si el valor dado es un número entero no negativo.

    Args:
        valor (str): Valor a validar.

    Returns:
        bool: True si es un número entero no negativo, False en caso contrario.
    '''
    # No puede tener punto decimal
    if '.' in valor:
        return False

    # Debe estar formado solo por dígitos
    if not valor.isdigit():
        return False

    return True


def guardar_libros(libros):
    '''
    Guarda la lista de libros en el archivo CSV.

    Args:
        libros (list[dict]): Lista de libros a guardar con claves 'TITULO' y 'CANTIDAD'.
    '''

    # Modo 'w' para sobrescribir el archivo con la nueva lista de libros
    with open(NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['TITULO', 'CANTIDAD'])
        escritor.writeheader()
        escritor.writerows(libros)


def mostrar_catalogo():
    '''
    Muestra en pantalla la lista de libros guardados en el archivo CSV.
    '''
    print('\nCatálogo de libros:')
    libros = obtener_libros()

    if not libros:
        print('No hay libros registrados.')
        return

    print('Título | Cantidad')
    print('-' * 40)
    for libro in libros:
        print(f"- {libro['TITULO']}: {libro['CANTIDAD']} ejemplar(es)")


def agregar_titulo():
    '''
    Solicita al usuario los datos de un nuevo libro y lo agrega al archivo CSV.
    Verifica que el libro no exista previamente y que la cantidad sea válida.
    '''
    print('\nAgregar nuevo título:')

    # Solicitar datos y validarlos
    titulo = input('Título del libro: ').strip()

    if not titulo:
        print('El título no puede estar vacío.')
        return

    if existe_libro(titulo):
        print(f'El libro "{titulo}" ya existe. No se puede agregar duplicados.')
        return

    cantidad = input('Cantidad de ejemplares: ').strip()

    if not validar_numero_entero_no_negativo(cantidad):
        print('Cantidad inválida. Debe ser un número entero mayor o igual a 0.')
        return

    # Convertir la cantidad a int antes de guardarlo
    cantidad = int(cantidad)

    agregar_libro({'TITULO': titulo, 'CANTIDAD': cantidad})
    print(f'Libro "{titulo}" agregado con éxito.')


def ingresar_titulos_multiples():
    '''
    Permite cargar varios libros de una vez.
    El usuario indica cuántos libros quiere cargar y por cada uno se pide título y cantidad.
    '''
    print('\nIngresar títulos (múltiples):')

    cantidad_libros = input('¿Cuántos libros desea cargar?: ').strip()

    if not validar_numero_entero_no_negativo(cantidad_libros):
        print('Cantidad inválida.')
        return

    cantidad_libros = int(cantidad_libros)

    if cantidad_libros <= 0:
        print('Debe ingresar al menos 1 libro.')
        return

    for i in range(cantidad_libros):
        print(f'\nLibro {i + 1}:')

        titulo = input('Título del libro: ').strip()

        if not titulo:
            print('El título no puede estar vacío. Libro no agregado.')
            continue

        if existe_libro(titulo):
            print(f'El libro "{titulo}" ya existe. No se puede agregar duplicados.')
            continue

        cantidad = input('Cantidad de ejemplares: ').strip()

        if not validar_numero_entero_no_negativo(cantidad):
            print('Cantidad inválida. Libro no agregado.')
            continue

        cantidad = int(cantidad)
        agregar_libro({'TITULO': titulo, 'CANTIDAD': cantidad})
        print(f'Libro "{titulo}" agregado con éxito.')


def ingresar_ejemplares():
    '''
    Suma una cantidad de ejemplares a un título existente.
    '''
    libros = obtener_libros()

    # Solicitar y validar el título del libro
    titulo = input('Ingrese el título del libro: ').strip()

    if not titulo:
        print('El título del libro no puede estar vacío.')
        return

    # Recorrer la lista de libros para encontrar el libro
    for libro in libros:
        if libro['TITULO'].lower() == titulo.lower():
            # Solicitar y validar la cantidad a agregar
            cantidad = input('Cantidad de ejemplares a agregar: ').strip()

            if not validar_numero_entero_no_negativo(cantidad):
                print('Cantidad inválida.')
                return

            cantidad = int(cantidad)

            # Sumar la cantidad al stock actual
            libro['CANTIDAD'] += cantidad

            # Escribir los cambios en el archivo CSV
            guardar_libros(libros)
            print(f'Se agregaron {cantidad} ejemplar(es) a "{titulo}". Stock actual: {libro["CANTIDAD"]}')
            break
    else:
        # Se ejecuta si el bucle no encontró el libro
        print(f'El libro "{titulo}" no existe.')


def consultar_disponibilidad():
    '''
    Busca un título y muestra cuántos ejemplares hay disponibles.
    '''
    titulo = input('Ingrese el título del libro a consultar: ').strip()

    if not titulo:
        print('El título del libro no puede estar vacío.')
        return

    libros = obtener_libros()

    # Buscar el libro en la lista
    for libro in libros:
        if libro['TITULO'].lower() == titulo.lower():
            print(f'"{libro["TITULO"]}" tiene {libro["CANTIDAD"]} ejemplar(es) disponible(s).')
            break
    else:
        print(f'El libro "{titulo}" no existe.')


def listar_agotados():
    '''
    Muestra solo los títulos con cantidad igual a 0.
    '''
    print('\nLibros agotados:')
    libros = obtener_libros()

    # Filtrar libros con cantidad 0
    agotados = []
    for libro in libros:
        if libro['CANTIDAD'] == 0:
            agotados.append(libro)

    if not agotados:
        print('No hay libros agotados.')
        return

    print('Título | Cantidad')
    print('-' * 40)
    for libro in agotados:
        print(f"- {libro['TITULO']}: {libro['CANTIDAD']} ejemplar(es)")


def actualizar_ejemplares():
    '''
    Permite realizar préstamo (restar 1) o devolución (sumar 1) de un libro.
    '''
    print('\nActualizar ejemplares (préstamo/devolución):')
    print('1. Préstamo (restar 1)')
    print('2. Devolución (sumar 1)')

    opcion = input('Ingrese una opción (1-2): ').strip()

    if opcion not in ['1', '2']:
        print('Opción inválida.')
        return

    titulo = input('Ingrese el título del libro: ').strip()

    if not titulo:
        print('El título del libro no puede estar vacío.')
        return

    libros = obtener_libros()

    # Buscar el libro en la lista
    for libro in libros:
        if libro['TITULO'].lower() == titulo.lower():
            if opcion == '1':
                # Préstamo: restar 1 solo si CANTIDAD > 0
                if libro['CANTIDAD'] > 0:
                    libro['CANTIDAD'] -= 1
                    guardar_libros(libros)
                    print(f'Préstamo realizado. Stock actual de "{libro["TITULO"]}": {libro["CANTIDAD"]} ejemplar(es).')
                else:
                    print(f'No hay ejemplares disponibles de "{libro["TITULO"]}" para préstamo.')
            else:
                # Devolución: sumar 1
                libro['CANTIDAD'] += 1
                guardar_libros(libros)
                print(f'Devolución realizada. Stock actual de "{libro["TITULO"]}": {libro["CANTIDAD"]} ejemplar(es).')
            break
    else:
        print(f'El libro "{titulo}" no existe.')


def mostrar_menu():
    '''
    Muestra el menú principal del Sistema de Gestión de Biblioteca.
    Permite al usuario seleccionar entre las diferentes opciones disponibles.
    '''

    while True:
        print('\n--- Menú de Gestión de Biblioteca ---')
        print('-' * 40)
        print('1. Ingresar títulos (múltiples)')
        print('2. Ingresar ejemplares')
        print('3. Mostrar catálogo')
        print('4. Consultar disponibilidad')
        print('5. Listar agotados')
        print('6. Agregar título')
        print('7. Actualizar ejemplares (préstamo/devolución)')
        print('8. Salir')
        print('-' * 40)

        opcion = input('Ingrese una opción (1-8): ').strip()

        match opcion:
            case '1':
                ingresar_titulos_multiples()
            case '2':
                ingresar_ejemplares()
            case '3':
                mostrar_catalogo()
            case '4':
                consultar_disponibilidad()
            case '5':
                listar_agotados()
            case '6':
                agregar_titulo()
            case '7':
                actualizar_ejemplares()
            case '8':
                print('Gracias por usar el sistema. ¡Hasta luego!')
                break
            case _:
                print('Opción inválida. Por favor, elija una opción del 1 al 8.')


# Iniciar el programa mostrando el menú
mostrar_menu()
