import csv
import os

# Obtener directorio del script para usar ruta absoluta
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NOMBRE_ARCHIVO = os.path.join(SCRIPT_DIR, 'paises.csv')

# Lista de continentes válidos para validación
CONTINENTES_VALIDOS = ['América', 'Europa', 'Asia', 'África', 'Oceanía']


def cargar_paises():
    '''
    Lee el archivo CSV y devuelve una lista de países como diccionarios.
    Si el archivo no existe, lo crea con los encabezados correspondientes.

    Returns:
        list[dict]: Lista de países con claves 'nombre', 'poblacion' (int), 'superficie' (int) y 'continente'.
    '''

    # Verificar si el archivo existe; si no, crearlo con encabezados
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'poblacion', 'superficie', 'continente'])
            escritor.writeheader()
            return []

    paises = []

    # Leer los países del archivo CSV
    with open(NOMBRE_ARCHIVO, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        # Agregar cada fila como un diccionario a la lista de países
        # Convertir población y superficie a int
        for fila in lector:
            paises.append({
                'nombre': fila['nombre'],
                'poblacion': int(fila['poblacion']),
                'superficie': int(fila['superficie']),
                'continente': fila['continente']
            })
    return paises


def guardar_paises(paises):
    '''
    Guarda la lista de países en el archivo CSV.

    Args:
        paises (list[dict]): Lista de países a guardar con claves 'nombre', 'poblacion', 'superficie' y 'continente'.
    '''

    # Modo 'w' para sobrescribir el archivo con la nueva lista de países
    with open(NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'poblacion', 'superficie', 'continente'])
        escritor.writeheader()
        escritor.writerows(paises)


def solicitar_texto_no_vacio(mensaje):
    '''
    Solicita al usuario un texto que no puede estar vacío.
    Loop bloqueante que re-solicita hasta obtener un valor válido.

    Args:
        mensaje (str): Mensaje a mostrar al usuario.

    Returns:
        str: Texto ingresado por el usuario (no vacío).
    '''
    texto = ''

    # Loop bloqueante hasta obtener texto válido
    while True:
        texto = input(mensaje).strip()

        if texto:
            break

        print('El texto no puede estar vacío. Por favor, intente nuevamente.')

    return texto


def solicitar_numero_positivo(mensaje):
    '''
    Solicita al usuario un número entero positivo.
    Loop bloqueante que re-solicita hasta obtener un valor válido.

    Args:
        mensaje (str): Mensaje a mostrar al usuario.

    Returns:
        int: Número entero positivo ingresado por el usuario.
    '''
    numero = 0

    # Loop bloqueante hasta obtener número válido
    while True:
        valor = input(mensaje).strip()

        # Validar que no tenga punto decimal
        if '.' in valor:
            print('Debe ingresar un número entero (sin decimales). Intente nuevamente.')
            continue

        # Validar que sea un número
        if not valor.isdigit():
            print('Debe ingresar un número válido. Intente nuevamente.')
            continue

        numero = int(valor)

        # Validar que sea positivo
        if numero <= 0:
            print('El número debe ser mayor a 0. Intente nuevamente.')
            continue

        break

    return numero


def solicitar_continente():
    '''
    Solicita al usuario un continente válido de la lista predefinida.
    Loop bloqueante que re-solicita hasta obtener un valor válido.

    Returns:
        str: Continente válido ingresado por el usuario.
    '''
    continente = ''

    # Mostrar opciones disponibles
    print('Continentes válidos:', ', '.join(CONTINENTES_VALIDOS))

    # Loop bloqueante hasta obtener continente válido
    while True:
        continente = input('Continente: ').strip()

        if not continente:
            print('El continente no puede estar vacío. Intente nuevamente.')
            continue

        # Buscar coincidencia en la lista de continentes válidos
        continente_encontrado = False
        i = 0
        while i < len(CONTINENTES_VALIDOS):
            if CONTINENTES_VALIDOS[i].lower() == continente.lower():
                continente = CONTINENTES_VALIDOS[i]  # Usar formato correcto
                continente_encontrado = True
                break
            i += 1

        if continente_encontrado:
            break

        print(f'Continente inválido. Debe ser uno de: {", ".join(CONTINENTES_VALIDOS)}')

    return continente


def existe_pais(paises, nombre):
    '''
    Verifica si un país con el nombre dado ya existe en la lista.

    Args:
        paises (list[dict]): Lista de países.
        nombre (str): Nombre del país a verificar.

    Returns:
        bool: True si el país existe, False en caso contrario.
    '''
    # Recorrer la lista de países usando while con contador manual
    i = 0
    while i < len(paises):
        if paises[i]['nombre'].lower() == nombre.strip().lower():
            return True
        i += 1

    return False


def agregar_pais(paises):
    '''
    Solicita al usuario los datos de un nuevo país y lo agrega a la lista.
    Verifica que el país no exista previamente y valida todos los campos.

    Args:
        paises (list[dict]): Lista actual de países.

    Returns:
        list[dict]: Lista de países actualizada con el nuevo país agregado.
    '''
    print('\n--- Agregar nuevo país ---')

    # Solicitar y validar nombre
    nombre = solicitar_texto_no_vacio('Nombre del país: ')

    # Verificar que no exista
    if existe_pais(paises, nombre):
        print(f'El país "{nombre}" ya existe en el sistema.')
        return paises

    # Solicitar y validar población
    poblacion = solicitar_numero_positivo('Población: ')

    # Solicitar y validar superficie
    superficie = solicitar_numero_positivo('Superficie (km²): ')

    # Solicitar y validar continente
    continente = solicitar_continente()

    # Crear nuevo país y agregarlo a la lista
    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }

    paises.append(nuevo_pais)

    # Guardar cambios en el archivo
    guardar_paises(paises)

    print(f'\nPaís "{nombre}" agregado exitosamente.')

    return paises


def mostrar_paises(paises):
    '''
    Muestra en pantalla la lista completa de países.

    Args:
        paises (list[dict]): Lista de países a mostrar.
    '''
    print('\n--- Catálogo de países ---')

    if not paises:
        print('No hay países registrados en el sistema.')
        return

    print(f'\nTotal de países: {len(paises)}')
    print('-' * 80)
    print(f"{'Nombre':<20} {'Población':<15} {'Superficie (km²)':<20} {'Continente':<15}")
    print('-' * 80)

    # Mostrar cada país usando while con contador manual
    i = 0
    while i < len(paises):
        pais = paises[i]
        print(f"{pais['nombre']:<20} {pais['poblacion']:<15,} {pais['superficie']:<20,} {pais['continente']:<15}")
        i += 1


def buscar_pais_por_nombre(paises):
    '''
    Busca países por nombre (coincidencia parcial o exacta) y muestra los resultados.

    Args:
        paises (list[dict]): Lista de países donde buscar.
    '''
    print('\n--- Buscar país por nombre ---')

    nombre_busqueda = solicitar_texto_no_vacio('Ingrese el nombre (o parte del nombre) a buscar: ')

    # Buscar coincidencias parciales o exactas
    resultados = []
    i = 0
    while i < len(paises):
        # Buscar coincidencia parcial (case insensitive)
        if nombre_busqueda.lower() in paises[i]['nombre'].lower():
            resultados.append(paises[i])
        i += 1

    # Mostrar resultados
    if not resultados:
        print(f'\nNo se encontraron países que contengan "{nombre_busqueda}".')
        return

    print(f'\nSe encontraron {len(resultados)} resultado(s):')
    print('-' * 80)
    print(f"{'Nombre':<20} {'Población':<15} {'Superficie (km²)':<20} {'Continente':<15}")
    print('-' * 80)

    i = 0
    while i < len(resultados):
        pais = resultados[i]
        print(f"{pais['nombre']:<20} {pais['poblacion']:<15,} {pais['superficie']:<20,} {pais['continente']:<15}")
        i += 1


def actualizar_pais(paises):
    '''
    Actualiza la población y/o superficie de un país existente.

    Args:
        paises (list[dict]): Lista de países.

    Returns:
        list[dict]: Lista de países actualizada.
    '''
    print('\n--- Actualizar datos de país ---')

    nombre = solicitar_texto_no_vacio('Nombre del país a actualizar: ')

    # Buscar el país en la lista usando while con contador manual
    pais_encontrado = None
    i = 0
    while i < len(paises):
        if paises[i]['nombre'].lower() == nombre.lower():
            pais_encontrado = paises[i]
            break
        i += 1

    if not pais_encontrado:
        print(f'\nEl país "{nombre}" no existe en el sistema.')
        return paises

    # Mostrar datos actuales
    print(f'\nDatos actuales de {pais_encontrado["nombre"]}:')
    print(f"Población: {pais_encontrado['poblacion']:,}")
    print(f"Superficie: {pais_encontrado['superficie']:,} km²")

    # Menú de opciones
    print('\n¿Qué desea actualizar?')
    print('1. Población')
    print('2. Superficie')
    print('3. Ambos')

    opcion = ''
    # Loop bloqueante para opción válida
    while True:
        opcion = input('Ingrese una opción (1-3): ').strip()
        if opcion in ['1', '2', '3']:
            break
        print('Opción inválida. Debe ingresar 1, 2 o 3.')

    # Actualizar según la opción elegida
    if opcion == '1' or opcion == '3':
        nueva_poblacion = solicitar_numero_positivo('Nueva población: ')
        pais_encontrado['poblacion'] = nueva_poblacion

    if opcion == '2' or opcion == '3':
        nueva_superficie = solicitar_numero_positivo('Nueva superficie (km²): ')
        pais_encontrado['superficie'] = nueva_superficie

    # Guardar cambios
    guardar_paises(paises)

    print(f'\nDatos de "{pais_encontrado["nombre"]}" actualizados exitosamente.')

    return paises


def filtrar_por_continente(paises):
    '''
    Filtra y muestra países de un continente específico.

    Args:
        paises (list[dict]): Lista de países.
    '''
    print('\n--- Filtrar por continente ---')

    continente = solicitar_continente()

    # Filtrar países del continente seleccionado
    resultados = []
    i = 0
    while i < len(paises):
        if paises[i]['continente'].lower() == continente.lower():
            resultados.append(paises[i])
        i += 1

    # Mostrar resultados
    if not resultados:
        print(f'\nNo hay países registrados en {continente}.')
        return

    print(f'\nPaíses de {continente} ({len(resultados)} encontrado(s)):')
    print('-' * 80)
    print(f"{'Nombre':<20} {'Población':<15} {'Superficie (km²)':<20} {'Continente':<15}")
    print('-' * 80)

    i = 0
    while i < len(resultados):
        pais = resultados[i]
        print(f"{pais['nombre']:<20} {pais['poblacion']:<15,} {pais['superficie']:<20,} {pais['continente']:<15}")
        i += 1


def filtrar_por_poblacion(paises):
    '''
    Filtra y muestra países dentro de un rango de población.

    Args:
        paises (list[dict]): Lista de países.
    '''
    print('\n--- Filtrar por rango de población ---')

    print('Ingrese el rango de población:')
    poblacion_min = solicitar_numero_positivo('Población mínima: ')
    poblacion_max = solicitar_numero_positivo('Población máxima: ')

    # Validar que el rango sea correcto
    if poblacion_min > poblacion_max:
        print('\nError: La población mínima no puede ser mayor que la máxima.')
        return

    # Filtrar países dentro del rango
    resultados = []
    i = 0
    while i < len(paises):
        if poblacion_min <= paises[i]['poblacion'] <= poblacion_max:
            resultados.append(paises[i])
        i += 1

    # Mostrar resultados
    if not resultados:
        print(f'\nNo hay países con población entre {poblacion_min:,} y {poblacion_max:,}.')
        return

    print(f'\nPaíses con población entre {poblacion_min:,} y {poblacion_max:,} ({len(resultados)} encontrado(s)):')
    print('-' * 80)
    print(f"{'Nombre':<20} {'Población':<15} {'Superficie (km²)':<20} {'Continente':<15}")
    print('-' * 80)

    i = 0
    while i < len(resultados):
        pais = resultados[i]
        print(f"{pais['nombre']:<20} {pais['poblacion']:<15,} {pais['superficie']:<20,} {pais['continente']:<15}")
        i += 1


def filtrar_por_superficie(paises):
    '''
    Filtra y muestra países dentro de un rango de superficie.

    Args:
        paises (list[dict]): Lista de países.
    '''
    print('\n--- Filtrar por rango de superficie ---')

    print('Ingrese el rango de superficie (km²):')
    superficie_min = solicitar_numero_positivo('Superficie mínima: ')
    superficie_max = solicitar_numero_positivo('Superficie máxima: ')

    # Validar que el rango sea correcto
    if superficie_min > superficie_max:
        print('\nError: La superficie mínima no puede ser mayor que la máxima.')
        return

    # Filtrar países dentro del rango
    resultados = []
    i = 0
    while i < len(paises):
        if superficie_min <= paises[i]['superficie'] <= superficie_max:
            resultados.append(paises[i])
        i += 1

    # Mostrar resultados
    if not resultados:
        print(f'\nNo hay países con superficie entre {superficie_min:,} y {superficie_max:,} km².')
        return

    print(f'\nPaíses con superficie entre {superficie_min:,} y {superficie_max:,} km² ({len(resultados)} encontrado(s)):')
    print('-' * 80)
    print(f"{'Nombre':<20} {'Población':<15} {'Superficie (km²)':<20} {'Continente':<15}")
    print('-' * 80)

    i = 0
    while i < len(resultados):
        pais = resultados[i]
        print(f"{pais['nombre']:<20} {pais['poblacion']:<15,} {pais['superficie']:<20,} {pais['continente']:<15}")
        i += 1


def ordenar_paises(paises):
    '''
    Ordena y muestra la lista de países según un criterio seleccionado.

    Args:
        paises (list[dict]): Lista de países.
    '''
    print('\n--- Ordenar países ---')

    if not paises:
        print('No hay países para ordenar.')
        return

    # Seleccionar criterio de ordenamiento
    print('\n¿Por qué criterio desea ordenar?')
    print('1. Nombre')
    print('2. Población')
    print('3. Superficie')

    criterio = ''
    # Loop bloqueante para criterio válido
    while True:
        criterio = input('Ingrese una opción (1-3): ').strip()
        if criterio in ['1', '2', '3']:
            break
        print('Opción inválida. Debe ingresar 1, 2 o 3.')

    # Seleccionar orden (ascendente/descendente)
    print('\n¿En qué orden?')
    print('1. Ascendente')
    print('2. Descendente')

    orden = ''
    # Loop bloqueante para orden válido
    while True:
        orden = input('Ingrese una opción (1-2): ').strip()
        if orden in ['1', '2']:
            break
        print('Opción inválida. Debe ingresar 1 o 2.')

    # Determinar si es orden descendente
    descendente = (orden == '2')

    # Crear copia de la lista para no modificar la original
    paises_ordenados = []
    i = 0
    while i < len(paises):
        paises_ordenados.append(paises[i].copy())
        i += 1

    # Ordenamiento burbuja (bubble sort)
    n = len(paises_ordenados)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            # Determinar si hay que intercambiar
            debe_intercambiar = False

            if criterio == '1':
                # Ordenar por nombre
                if descendente:
                    debe_intercambiar = paises_ordenados[j]['nombre'].lower() < paises_ordenados[j + 1]['nombre'].lower()
                else:
                    debe_intercambiar = paises_ordenados[j]['nombre'].lower() > paises_ordenados[j + 1]['nombre'].lower()
                criterio_texto = 'nombre'

            elif criterio == '2':
                # Ordenar por población
                if descendente:
                    debe_intercambiar = paises_ordenados[j]['poblacion'] < paises_ordenados[j + 1]['poblacion']
                else:
                    debe_intercambiar = paises_ordenados[j]['poblacion'] > paises_ordenados[j + 1]['poblacion']
                criterio_texto = 'población'

            else:
                # Ordenar por superficie
                if descendente:
                    debe_intercambiar = paises_ordenados[j]['superficie'] < paises_ordenados[j + 1]['superficie']
                else:
                    debe_intercambiar = paises_ordenados[j]['superficie'] > paises_ordenados[j + 1]['superficie']
                criterio_texto = 'superficie'

            # Realizar intercambio si es necesario (swap)
            if debe_intercambiar:
                temp = paises_ordenados[j]
                paises_ordenados[j] = paises_ordenados[j + 1]
                paises_ordenados[j + 1] = temp

            j += 1
        i += 1

    orden_texto = 'descendente' if descendente else 'ascendente'

    # Mostrar resultados ordenados
    print(f'\nPaíses ordenados por {criterio_texto} ({orden_texto}):')
    print('-' * 80)
    print(f"{'Nombre':<20} {'Población':<15} {'Superficie (km²)':<20} {'Continente':<15}")
    print('-' * 80)

    i = 0
    while i < len(paises_ordenados):
        pais = paises_ordenados[i]
        print(f"{pais['nombre']:<20} {pais['poblacion']:<15,} {pais['superficie']:<20,} {pais['continente']:<15}")
        i += 1


def mostrar_estadisticas(paises):
    '''
    Calcula y muestra estadísticas sobre los países registrados.

    Args:
        paises (list[dict]): Lista de países.
    '''
    print('\n--- Estadísticas ---')

    if not paises:
        print('No hay países registrados para calcular estadísticas.')
        return

    # Encontrar país con mayor población
    pais_mayor_poblacion = paises[0]
    i = 1
    while i < len(paises):
        if paises[i]['poblacion'] > pais_mayor_poblacion['poblacion']:
            pais_mayor_poblacion = paises[i]
        i += 1

    # Encontrar país con menor población
    pais_menor_poblacion = paises[0]
    i = 1
    while i < len(paises):
        if paises[i]['poblacion'] < pais_menor_poblacion['poblacion']:
            pais_menor_poblacion = paises[i]
        i += 1

    # Calcular promedio de población
    suma_poblacion = 0
    i = 0
    while i < len(paises):
        suma_poblacion += paises[i]['poblacion']
        i += 1
    promedio_poblacion = suma_poblacion / len(paises)

    # Calcular promedio de superficie
    suma_superficie = 0
    i = 0
    while i < len(paises):
        suma_superficie += paises[i]['superficie']
        i += 1
    promedio_superficie = suma_superficie / len(paises)

    # Contar países por continente
    conteo_continentes = {}
    i = 0
    while i < len(paises):
        continente = paises[i]['continente']
        if continente in conteo_continentes:
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1
        i += 1

    # Mostrar estadísticas
    print(f'\nTotal de países registrados: {len(paises)}')
    print('-' * 60)

    print(f'\nPaís con mayor población:')
    print(f"  {pais_mayor_poblacion['nombre']}: {pais_mayor_poblacion['poblacion']:,} habitantes")

    print(f'\nPaís con menor población:')
    print(f"  {pais_menor_poblacion['nombre']}: {pais_menor_poblacion['poblacion']:,} habitantes")

    print(f'\nPromedio de población: {promedio_poblacion:,.0f} habitantes')
    print(f'Promedio de superficie: {promedio_superficie:,.0f} km²')

    print(f'\nCantidad de países por continente:')
    # Mostrar conteo por continente usando while
    continentes = list(conteo_continentes.keys())
    i = 0
    while i < len(continentes):
        continente = continentes[i]
        print(f"  {continente}: {conteo_continentes[continente]} país(es)")
        i += 1


def mostrar_menu():
    '''
    Muestra el menú principal del Sistema de Gestión de Países.
    Permite al usuario seleccionar entre las diferentes opciones disponibles.
    '''

    # Cargar países al inicio (una sola vez)
    paises = cargar_paises()

    while True:
        print('\n' + '=' * 60)
        print('SISTEMA DE GESTIÓN DE PAÍSES')
        print('=' * 60)
        print('1.  Agregar país')
        print('2.  Actualizar población/superficie de un país')
        print('3.  Buscar país por nombre')
        print('4.  Filtrar por continente')
        print('5.  Filtrar por rango de población')
        print('6.  Filtrar por rango de superficie')
        print('7.  Ordenar países')
        print('8.  Mostrar estadísticas')
        print('9.  Mostrar todos los países')
        print('10. Salir')
        print('=' * 60)

        opcion = input('Ingrese una opción (1-10): ').strip()

        match opcion:
            case '1':
                paises = agregar_pais(paises)
            case '2':
                paises = actualizar_pais(paises)
            case '3':
                buscar_pais_por_nombre(paises)
            case '4':
                filtrar_por_continente(paises)
            case '5':
                filtrar_por_poblacion(paises)
            case '6':
                filtrar_por_superficie(paises)
            case '7':
                ordenar_paises(paises)
            case '8':
                mostrar_estadisticas(paises)
            case '9':
                mostrar_paises(paises)
            case '10':
                print('\n¡Gracias por usar el Sistema de Gestión de Países!')
                print('Hasta luego.\n')
                break
            case _:
                print('\nOpción inválida. Por favor, elija una opción del 1 al 10.')


# Iniciar el programa mostrando el menú
mostrar_menu()
