# ========================================================================
# TRABAJO PRACTICO INTEGRADOR - PROGRAMACION 1
# Sistema de Gestión de Países
# ========================================================================
#
# Autores: Aguero Maximiliano y Dario Frison
# Materia: Programación 1 - UTN
#
# ========================================================================
# OBJETIVO
# ========================================================================
# Desarrollar una aplicación en Python que permita gestionar información 
# sobre países, aplicando listas, diccionarios, funciones, estructuras 
# condicionales y repetitivas, ordenamientos y estadísticas.
#
# ========================================================================
# ESTRUCTURAS UTILIZADAS
# ========================================================================
# - Listas: para almacenar la colección de países
# - Diccionarios: para representar cada país con sus datos
# - Funciones: para organizar el código en bloques reutilizables
# - Estructuras condicionales (if/elif/else, match/case)
# - Estructuras repetitivas (for, while)
# - Ordenamiento burbuja (Bubble Sort)
# - Lectura de archivos CSV sin usar librerías externas
#
# ========================================================================
# FUNCIONALIDADES
# ========================================================================
# 1. Gestión de datos:
#    - Cargar países desde archivo CSV
#    - Agregar países manualmente
#    - Actualizar datos de países
#
# 2. Consultas y búsquedas:
#    - Buscar países por nombre
#    - Filtrar por continente, población o superficie
#
# 3. Ordenamiento:
#    - Ordenar por nombre, población o superficie
#
# 4. Estadísticas:
#    - Calcular promedios, máximos y mínimos
#    - Distribución por continentes
#
# ========================================================================

# ========================== GESTIÓN DE PAÍSES ==========================

# Lista global para almacenar los países
paises = []

# ========================== FUNCIONES DE LECTURA DE ARCHIVOS ==========================

def leer_csv(nombre_archivo):
    """
    Lee un archivo CSV y carga los datos de países en la lista global.
    
    Formato esperado del CSV:
        nombre,poblacion,superficie,continente
        Argentina,45000000,2780400,América del Sur
    """
    global paises
    paises_cargados = 0
    errores_encontrados = []
    
    # Abrir y leer el archivo
    archivo = open(nombre_archivo, 'r' , encoding='utf-8')
    lineas = archivo.readlines()
    archivo.close()
    
    if len(lineas) == 0:
        print("Error: El archivo esta vacio.")
        return False
    
    # Procesar cada línea del CSV
    for i in range(len(lineas)):
        linea = lineas[i].strip()
        
        # Saltar líneas vacías o encabezado
        if linea == "":
            continue
        
        linea_minuscula = linea.lower()
        if i == 0 and ('nombre' in linea_minuscula or 'pais' in linea_minuscula or 'poblacion' in linea_minuscula):
            continue
        
        # Extraer y limpiar campos
        campos = linea.split(',')
        for j in range(len(campos)):
            campos[j] = campos[j].strip()
        
        # Validar estructura: debe tener 4 campos (nombre, población, superficie, continente)
        if len(campos) != 4:
            error = f"Linea {i+1}: Se esperan 4 campos, se encontraron {len(campos)}"
            errores_encontrados.append(error)
            continue
        
        nombre = campos[0]
        poblacion_str = campos[1]
        superficie_str = campos[2]
        continente = campos[3]
        
        # Validar que no haya campos vacíos
        if nombre == "" or poblacion_str == "" or superficie_str == "" or continente == "":
            error = f"Linea {i+1}: Campos vacios no permitidos"
            errores_encontrados.append(error)
            continue
        
        # Validar que población y superficie sean números enteros
        es_numero_pob = True
        for caracter in poblacion_str:
            if caracter < '0' or caracter > '9':
                es_numero_pob = False
                break
        
        es_numero_sup = True
        for caracter in superficie_str:
            if caracter < '0' or caracter > '9':
                es_numero_sup = False
                break
        
        if not es_numero_pob or not es_numero_sup:
            error = f"Linea {i+1}: Poblacion y superficie deben ser numeros enteros"
            errores_encontrados.append(error)
            continue
        
        poblacion = int(poblacion_str)
        superficie = int(superficie_str)
        
        # Regla de negocio: no existen países con población o superficie cero o negativa
        if poblacion <= 0 or superficie <= 0:
            error = f"Linea {i+1}: Poblacion y superficie deben ser numeros positivos"
            errores_encontrados.append(error)
            continue
        
        # Crear diccionario del país y agregarlo a la lista
        pais = {
            'nombre': nombre.title(),
            'poblacion': poblacion,
            'superficie': superficie,
            'continente': continente.title()
        }
        
        paises.append(pais)
        paises_cargados = paises_cargados + 1
    
    # Mostrar resumen del resultado
    print("\n" + "="*60)
    print("           RESULTADO DE CARGA DE ARCHIVO")
    print("="*60)
    
    if paises_cargados > 0:
        print(f"Paises cargados exitosamente: {paises_cargados}")
    
    if len(errores_encontrados) > 0:
        print(f"Errores encontrados: {len(errores_encontrados)}")
        print("\nDetalle de errores:")
        
        limite = 5 if len(errores_encontrados) >= 5 else len(errores_encontrados)
        
        for j in range(limite):
            print(f"  {errores_encontrados[j]}")
        
        if len(errores_encontrados) > 5:
            print(f"  ... y {len(errores_encontrados) - 5} errores mas")
    
    if paises_cargados == 0:
        print("No se pudo cargar ningun pais del archivo.")
    
    print("="*60)
    
    return paises_cargados > 0

# ========================== FUNCIONES AUXILIARES ==========================

def es_numero(texto):
    """
    Verifica si un texto contiene solo dígitos.
    """
    if texto == "":
        return False
    
    for caracter in texto:
        if caracter < '0' or caracter > '9':
            return False
    
    return True

def buscar_pais_por_nombre_exacto(nombre_buscar):
    """
    Busca un país por nombre exacto.
    """
    nombre_minuscula = nombre_buscar.strip().lower()
    
    for pais in paises:
        if pais['nombre'].lower() == nombre_minuscula:
            return pais
    
    return None

def obtener_continentes_unicos():
    """
    Obtiene lista de continentes únicos ordenada alfabéticamente.
    Útil para mostrar opciones al usuario y hacer estadísticas por continente.
    """
    continentes = []
    
    # Extraer continentes únicos
    for pais in paises:
        continente = pais['continente']
        
        esta = False
        for c in continentes:
            if c == continente:
                esta = True
                break
        
        if not esta:
            continentes.append(continente)
    
    # Ordenar alfabéticamente
    for i in range(len(continentes)):
        for j in range(i + 1, len(continentes)):
            if continentes[i] > continentes[j]:
                temp = continentes[i]
                continentes[i] = continentes[j]
                continentes[j] = temp
    
    return continentes

# ========================== FUNCIONES DE GESTIÓN DE PAÍSES ==========================

def agregar_pais():
    """
    Solicita datos al usuario y agrega un nuevo país a la lista.
    Valida que todos los campos sean correctos y que el país no exista previamente.
    """
    print("\n" + "="*50)
    print("AGREGAR NUEVO PAIS".center(50))
    print("="*50)
    
    # Solicitar y validar nombre (no vacío, sin duplicados)
    while True:
        nombre = input("Ingrese el nombre del pais: ").strip()
        
        if nombre == "":
            print("Error: El nombre no puede estar vacio.")
            continue
        
        nombre = nombre.title()
        
        if buscar_pais_por_nombre_exacto(nombre):
            print(f"Error: El pais '{nombre}' ya existe en la base de datos.")
            continue
        
        break
    
    # Solicitar y validar población (número entero positivo)
    while True:
        poblacion_str = input("Ingrese la poblacion: ").strip()
        
        if not es_numero(poblacion_str):
            print("Error: La poblacion debe ser un numero entero valido.")
            continue
        
        poblacion = int(poblacion_str)
        
        if poblacion <= 0:
            print("Error: La poblacion debe ser mayor a 0.")
            continue
        
        break
    
    # Solicitar y validar superficie (número entero positivo)
    while True:
        superficie_str = input("Ingrese la superficie (km2): ").strip()
        
        if not es_numero(superficie_str):
            print("Error: La superficie debe ser un numero entero valido.")
            continue
        
        superficie = int(superficie_str)
        
        if superficie <= 0:
            print("Error: La superficie debe ser mayor a 0.")
            continue
        
        break
    
    # Mostrar continentes existentes como ayuda
    continentes_existentes = obtener_continentes_unicos()
    if len(continentes_existentes) > 0:
        print("\nContinentes existentes:", end=" ")
        for i in range(len(continentes_existentes)):
            if i > 0:
                print(",", end=" ")
            print(continentes_existentes[i], end="")
        print()
    
    # Solicitar y validar continente (no vacío)
    while True:
        continente = input("Ingrese el continente: ").strip()
        if continente == "":
            print("Error: El continente no puede estar vacio.")
            continue
        
        continente = continente.title()
        break
    
    # Crear y agregar el nuevo país
    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    
    paises.append(nuevo_pais)
    
    print("\n" + "="*50)
    print(f"Pais '{nombre}' agregado exitosamente!")
    print("="*50)

def actualizar_pais():
    """
    Permite actualizar la población y superficie de un país existente.
    """
    print("\n" + "="*50)
    print("ACTUALIZAR DATOS DE PAIS".center(50))
    print("="*50)
    
    if len(paises) == 0:
        print("No hay paises cargados en el sistema.")
        return
    
    # Solicitar y validar nombre del país
    while True:
        nombre_buscar = input("Ingrese el nombre del pais a actualizar: ").strip()
        if nombre_buscar == "":
            print("Debe ingresar un nombre valido.")
            continue
        break
    
    pais_encontrado = buscar_pais_por_nombre_exacto(nombre_buscar)
    
    if pais_encontrado == None:
        print(f"No se encontro el pais '{nombre_buscar}'.")
        print("Verifique la ortografia o use la opcion de busqueda.")
        return
    
    # Mostrar datos actuales
    print(f"\nDatos actuales de {pais_encontrado['nombre']}:")
    print(f"   Poblacion: {pais_encontrado['poblacion']:,} habitantes")
    print(f"   Superficie: {pais_encontrado['superficie']:,} km2")
    print(f"   Continente: {pais_encontrado['continente']}")
    
    # Actualizar población si se ingresa un valor
    print("\nActualizacion de poblacion:")
    nueva_poblacion_str = input("Nueva poblacion (Enter para mantener actual): ").strip()
    
    if nueva_poblacion_str != "":
        if es_numero(nueva_poblacion_str):
            nueva_poblacion = int(nueva_poblacion_str)
            if nueva_poblacion > 0:
                pais_encontrado['poblacion'] = nueva_poblacion
                print(f"Poblacion actualizada a {nueva_poblacion:,} habitantes.")
            else:
                print("Error: La poblacion debe ser mayor a 0. No se actualizo.")
        else:
            print("Error: Debe ingresar un numero. No se actualizo.")
    
    # Actualizar superficie si se ingresa un valor
    print("\nActualizacion de superficie:")
    nueva_superficie_str = input("Nueva superficie en km2 (Enter para mantener actual): ").strip()
    
    if nueva_superficie_str != "":
        if es_numero(nueva_superficie_str):
            nueva_superficie = int(nueva_superficie_str)
            if nueva_superficie > 0:
                pais_encontrado['superficie'] = nueva_superficie
                print(f"Superficie actualizada a {nueva_superficie:,} km2.")
            else:
                print("Error: La superficie debe ser mayor a 0. No se actualizo.")
        else:
            print("Error: Debe ingresar un numero. No se actualizo.")
    
    print("\n" + "="*50)
    print("Pais actualizado exitosamente.")
    print("="*50)

def buscar_pais():
    """
    Busca países por nombre usando coincidencia parcial o exacta.
    """
    print("\n" + "="*50)
    print("BUSCAR PAIS POR NOMBRE".center(50))
    print("="*50)
    
    if len(paises) == 0:
        print("Error: No hay paises cargados en el sistema.")
        return
    
    # Solicitar nombre a buscar
    nombre_buscar = ""
    while nombre_buscar == "":
        nombre_buscar = input("Ingrese el nombre del pais a buscar: ").strip()
        if nombre_buscar == "":
            print("Error: Debe ingresar un nombre para buscar.")
    
    nombre_buscar_minuscula = nombre_buscar.lower()
    
    # Buscar coincidencias exactas y parciales
    coincidencias_exactas = []
    coincidencias_parciales = []
    
    for pais in paises:
        nombre_pais_minuscula = pais['nombre'].lower()
        
        if nombre_pais_minuscula == nombre_buscar_minuscula:
            coincidencias_exactas.append(pais)
        elif nombre_buscar_minuscula in nombre_pais_minuscula:
            coincidencias_parciales.append(pais)
    
    # Mostrar resultados según coincidencias encontradas
    total_resultados = len(coincidencias_exactas) + len(coincidencias_parciales)
    
    if total_resultados > 0:
        print(f"\nSe encontraron {total_resultados} resultado(s) para '{nombre_buscar}':")
        
        if len(coincidencias_exactas) > 0:
            print(f"\nCoincidencias exactas ({len(coincidencias_exactas)}):")
            mostrar_paises(coincidencias_exactas)
        
        if len(coincidencias_parciales) > 0:
            print(f"\nCoincidencias parciales ({len(coincidencias_parciales)}):")
            mostrar_paises(coincidencias_parciales)
    else:
        print(f"\nNo se encontraron paises que contengan '{nombre_buscar}'.")
        
        # Sugerir países disponibles ordenados alfabéticamente
        print("\nPaises disponibles en el sistema:")
        
        nombres_disponibles = []
        for pais in paises:
            nombres_disponibles.append(pais['nombre'])
        
        for i in range(len(nombres_disponibles)):
            for j in range(i + 1, len(nombres_disponibles)):
                if nombres_disponibles[i] > nombres_disponibles[j]:
                    temp = nombres_disponibles[i]
                    nombres_disponibles[i] = nombres_disponibles[j]
                    nombres_disponibles[j] = temp
        
        limite = 10
        if len(nombres_disponibles) < 10:
            limite = len(nombres_disponibles)
        
        for i in range(limite):
            print(f"  - {nombres_disponibles[i]}")
        
        if len(nombres_disponibles) > 10:
            print(f"  ... y {len(nombres_disponibles) - 10} mas")

# ========================== FUNCIONES DE FILTRADO ==========================

def filtrar_por_continente():
    """
    Filtra países por continente.
    """
    print("\n" + "="*50)
    print("FILTRAR POR CONTINENTE".center(50))
    print("="*50)
    
    if len(paises) == 0:
        print("No hay paises cargados en el sistema.")
        return
    
    # Mostrar continentes disponibles con contador
    continentes_disponibles = obtener_continentes_unicos()
    print("Continentes disponibles:")
    
    for i in range(len(continentes_disponibles)):
        continente = continentes_disponibles[i]
        contador = 0
        for pais in paises:
            if pais['continente'] == continente:
                contador = contador + 1
        
        print(f"  {i+1}. {continente} ({contador} paises)")
    
    # Solicitar continente a filtrar
    while True:
        continente_buscar = input("\nIngrese el continente: ").strip()
        if continente_buscar != "":
            break
        print("Debe ingresar un continente.")
    
    # Filtrar países por continente
    continente_minuscula = continente_buscar.lower()
    resultados = []
    
    for pais in paises:
        if pais['continente'].lower() == continente_minuscula:
            resultados.append(pais)
    
    if len(resultados) > 0:
        continente_encontrado = resultados[0]['continente']
        print(f"\nPaises en {continente_encontrado} ({len(resultados)} paises):")
        mostrar_paises(resultados)
    else:
        print(f"\nNo se encontraron paises en '{continente_buscar}'.")
        print("Verifique la ortografia o seleccione de la lista mostrada arriba.")

def filtrar_por_poblacion():
    """
    Filtra países por rango de población.
    Muestra solo los países cuya población esté entre los valores ingresados por el usuario.
    """
    print("\n" + "="*50)
    print("FILTRAR POR RANGO DE POBLACION".center(50))
    print("="*50)
    
    if len(paises) == 0:
        print("No hay paises cargados en el sistema.")
        return
    
    # Calcular y mostrar rango de poblaciones disponibles
    poblacion_min = paises[0]['poblacion']
    poblacion_max = paises[0]['poblacion']
    
    for pais in paises:
        if pais['poblacion'] < poblacion_min:
            poblacion_min = pais['poblacion']
        if pais['poblacion'] > poblacion_max:
            poblacion_max = pais['poblacion']
    
    print(f"Rango de poblaciones en el sistema:")
    print(f"  Minima: {poblacion_min:,} habitantes")
    print(f"  Maxima: {poblacion_max:,} habitantes")
    
    # Solicitar población mínima del rango
    while True:
        min_poblacion_str = input("\nPoblacion minima: ").strip()
        
        if not es_numero(min_poblacion_str):
            print("Error: Debe ingresar un numero entero valido.")
            continue
        
        min_poblacion = int(min_poblacion_str)
        
        if min_poblacion <= 0:
            print("Error: La poblacion debe ser mayor a 0.")
            continue
        
        break
    
    # Solicitar población máxima del rango
    while True:
        max_poblacion_str = input("Poblacion maxima: ").strip()
        
        if not es_numero(max_poblacion_str):
            print("Error: Debe ingresar un numero entero valido.")
            continue
        
        max_poblacion = int(max_poblacion_str)
        
        if max_poblacion <= 0:
            print("Error: La poblacion debe ser mayor a 0.")
            continue
        
        break
    
    # Validar que el rango sea lógico
    if min_poblacion > max_poblacion:
        print("Error: La poblacion minima no puede ser mayor que la maxima.")
        print(f"  Minimo ingresado: {min_poblacion}")
        print(f"  Maximo ingresado: {max_poblacion}")
        return
    
    # Filtrar países dentro del rango
    resultados = []
    for pais in paises:
        if pais['poblacion'] >= min_poblacion and pais['poblacion'] <= max_poblacion:
            resultados.append(pais)
    
    # Mostrar resultados
    if len(resultados) > 0:
        print(f"\nPaises con poblacion entre {min_poblacion:,} y {max_poblacion:,} habitantes:")
        print(f"Se encontraron {len(resultados)} paises.")
        mostrar_paises(resultados)
    else:
        print(f"\nNo se encontraron paises en el rango de {min_poblacion:,} a {max_poblacion:,} habitantes.")

def filtrar_por_superficie():
    """
    Filtra países por rango de superficie.
    """
    print("\n" + "="*50)
    print("FILTRAR POR RANGO DE SUPERFICIE".center(50))
    print("="*50)
    
    if len(paises) == 0:
        print("No hay paises cargados en el sistema.")
        return
    
    # Calcular rango de superficies disponibles
    superficie_min = paises[0]['superficie']
    superficie_max = paises[0]['superficie']
    
    for pais in paises:
        if pais['superficie'] < superficie_min:
            superficie_min = pais['superficie']
        if pais['superficie'] > superficie_max:
            superficie_max = pais['superficie']
    
    print(f"Rango de superficies en el sistema:")
    print(f"  Minima: {superficie_min:,} km2")
    print(f"  Maxima: {superficie_max:,} km2")
    
    # Solicitar superficie mínima del rango
    while True:
        min_superficie_str = input("\nSuperficie minima (km2): ").strip()
        
        if not es_numero(min_superficie_str):
            print("Error: Debe ingresar un numero entero valido.")
            continue
        
        min_superficie = int(min_superficie_str)
        
        if min_superficie <= 0:
            print("Error: La superficie debe ser mayor a 0.")
            continue
        
        break
    
    # Solicitar superficie máxima del rango
    while True:
        max_superficie_str = input("Superficie maxima (km2): ").strip()
        
        if not es_numero(max_superficie_str):
            print("Error: Debe ingresar un numero entero valido.")
            continue
        
        max_superficie = int(max_superficie_str)
        
        if max_superficie <= 0:
            print("Error: La superficie debe ser mayor a 0.")
            continue
        
        break
    
    # Validar que el rango sea lógico
    if min_superficie > max_superficie:
        print("Error: La superficie minima no puede ser mayor que la maxima.")
        print(f"  Minimo ingresado: {min_superficie}")
        print(f"  Maximo ingresado: {max_superficie}")
        return
    
    # Filtrar países dentro del rango
    resultados = []
    for pais in paises:
        if pais['superficie'] >= min_superficie and pais['superficie'] <= max_superficie:
            resultados.append(pais)
    
    if len(resultados) > 0:
        print(f"\nPaises con superficie entre {min_superficie:,} y {max_superficie:,} km2:")
        print(f"Se encontraron {len(resultados)} paises.")
        mostrar_paises(resultados)
    else:
        print(f"\nNo se encontraron paises en el rango de {min_superficie:,} a {max_superficie:,} km2.")

# ========================== FUNCIONES DE ORDENAMIENTO ==========================

def ordenar_paises_por_criterio(lista_paises, criterio, ascendente):
    """
    Ordena una lista de países por un criterio específico usando el algoritmo de burbuja.
    
    Parámetros:
        lista_paises: lista de diccionarios de países a ordenar
        criterio: 'nombre', 'poblacion' o 'superficie'
        ascendente: True para orden ascendente (A-Z, menor a mayor)
                   False para orden descendente (Z-A, mayor a menor)
    
    Retorna: una nueva lista ordenada sin modificar la original
    """
    if len(lista_paises) == 0:
        return []
    
    # Crear copia de la lista para no modificar la original
    paises_ordenados = []
    for pais in lista_paises:
        paises_ordenados.append(pais)
    
    n = len(paises_ordenados)
    
    # Aplicar ordenamiento burbuja (Bubble Sort)
    # El algoritmo compara elementos adyacentes y los intercambia si están en orden incorrecto
    for i in range(n - 1):
        # En cada pasada, el elemento más grande/pequeño "burbujea" hacia el final
        for j in range(n - 1 - i):
            # Determinar si se debe hacer el intercambio según el orden deseado
            debe_intercambiar = False
            
            if ascendente:
                # Para orden ascendente: intercambiar si el actual es mayor que el siguiente
                if paises_ordenados[j][criterio] > paises_ordenados[j + 1][criterio]:
                    debe_intercambiar = True
            else:
                # Para orden descendente: intercambiar si el actual es menor que el siguiente
                if paises_ordenados[j][criterio] < paises_ordenados[j + 1][criterio]:
                    debe_intercambiar = True
            
            # Realizar el intercambio si es necesario
            if debe_intercambiar:
                temp = paises_ordenados[j]
                paises_ordenados[j] = paises_ordenados[j + 1]
                paises_ordenados[j + 1] = temp
    
    return paises_ordenados

def ordenar_por_nombre():
    """
    Ordena países por nombre alfabéticamente.
    """
    print("\n" + "="*50)
    print("ORDENAR POR NOMBRE".center(50))
    print("="*50)
    
    if len(paises) == 0:
        print("No hay paises cargados en el sistema.")
        return
    
    print("Ordenando paises por nombre...")
    paises_ordenados = ordenar_paises_por_criterio(paises, 'nombre', True)
    
    print(f"\nPaises ordenados alfabeticamente ({len(paises_ordenados)} paises):")
    mostrar_paises(paises_ordenados)

def ordenar_por_poblacion():
    """
    Ordena países por población.
    """
    print("\n" + "="*50)
    print("ORDENAR POR POBLACION".center(50))
    print("="*50)
    
    if len(paises) == 0:
        print("No hay paises cargados en el sistema.")
        return
    
    print("Seleccione el tipo de ordenamiento:")
    print("1. Ascendente (menor a mayor poblacion)")
    print("2. Descendente (mayor a menor poblacion)")
    
    while True:
        opcion = input("Ingrese su opcion (1 o 2): ").strip()
        if opcion == '1' or opcion == '2':
            break
        print("Opcion invalida. Ingrese 1 o 2.")
    
    if opcion == '1':
        ascendente = True
        direccion_texto = "ascendente (menor a mayor)"
    else:
        ascendente = False
        direccion_texto = "descendente (mayor a menor)"
    
    print(f"Ordenando paises por poblacion ({direccion_texto})...")
    paises_ordenados = ordenar_paises_por_criterio(paises, 'poblacion', ascendente)
    
    print(f"\nPaises ordenados por poblacion - {direccion_texto}:")
    mostrar_paises(paises_ordenados)

def ordenar_por_superficie():
    """
    Ordena países por superficie.
    """
    print("\n" + "="*50)
    print("ORDENAR POR SUPERFICIE".center(50))
    print("="*50)
    
    if len(paises) == 0:
        print("No hay paises cargados en el sistema.")
        return
    
    print("Seleccione el tipo de ordenamiento:")
    print("1. Ascendente (menor a mayor superficie)")
    print("2. Descendente (mayor a menor superficie)")
    
    while True:
        opcion = input("Ingrese su opcion (1 o 2): ").strip()
        if opcion == '1' or opcion == '2':
            break
        print("Opcion invalida. Ingrese 1 o 2.")
    
    if opcion == '1':
        ascendente = True
        direccion_texto = "ascendente (menor a mayor)"
    else:
        ascendente = False
        direccion_texto = "descendente (mayor a menor)"
    
    print(f"Ordenando paises por superficie ({direccion_texto})...")
    paises_ordenados = ordenar_paises_por_criterio(paises, 'superficie', ascendente)
    
    print(f"\nPaises ordenados por superficie - {direccion_texto}:")
    mostrar_paises(paises_ordenados)

# ========================== FUNCIONES DE ESTADÍSTICAS ==========================

def mostrar_estadisticas():
    """
    Calcula y muestra estadísticas completas sobre los países cargados.
    Incluye análisis de población, superficie y distribución por continentes.
    """
    print("\n" + "="*60)
    print("ESTADISTICAS GENERALES".center(60))
    print("="*60)
    
    if len(paises) == 0:
        print("No hay paises cargados en el sistema.")
        return
    
    # Calcular estadísticas de población
    pais_mayor_poblacion = paises[0]
    pais_menor_poblacion = paises[0]
    total_poblacion = 0
    
    for pais in paises:
        total_poblacion = total_poblacion + pais['poblacion']
        
        if pais['poblacion'] > pais_mayor_poblacion['poblacion']:
            pais_mayor_poblacion = pais
        
        if pais['poblacion'] < pais_menor_poblacion['poblacion']:
            pais_menor_poblacion = pais
    
    promedio_poblacion = total_poblacion / len(paises)
    
    # Calcular estadísticas de superficie
    pais_mayor_superficie = paises[0]
    pais_menor_superficie = paises[0]
    total_superficie = 0
    
    for pais in paises:
        total_superficie = total_superficie + pais['superficie']
        
        if pais['superficie'] > pais_mayor_superficie['superficie']:
            pais_mayor_superficie = pais
        
        if pais['superficie'] < pais_menor_superficie['superficie']:
            pais_menor_superficie = pais
    
    promedio_superficie = total_superficie / len(paises)
    
    # Mostrar estadísticas de población
    print("\nESTADISTICAS DE POBLACION:")
    print("-" * 50)
    print(f"Pais con mayor poblacion: {pais_mayor_poblacion['nombre']}")
    print(f"  Poblacion: {pais_mayor_poblacion['poblacion']:,} habitantes")
    print(f"Pais con menor poblacion: {pais_menor_poblacion['nombre']}")
    print(f"  Poblacion: {pais_menor_poblacion['poblacion']:,} habitantes")
    print(f"Poblacion promedio: {promedio_poblacion:,.0f} habitantes")
    print(f"Poblacion total: {total_poblacion:,} habitantes")
    
    # Mostrar estadísticas de superficie
    print("\nESTADISTICAS DE SUPERFICIE:")
    print("-" * 50)
    print(f"Pais con mayor superficie: {pais_mayor_superficie['nombre']}")
    print(f"  Superficie: {pais_mayor_superficie['superficie']:,} km2")
    print(f"Pais con menor superficie: {pais_menor_superficie['nombre']}")
    print(f"  Superficie: {pais_menor_superficie['superficie']:,} km2")
    print(f"Superficie promedio: {promedio_superficie:,.0f} km2")
    print(f"Superficie total: {total_superficie:,} km2")
    
    # Calcular y mostrar distribución por continentes
    continentes = obtener_continentes_unicos()
    
    print("\nDISTRIBUCION POR CONTINENTES:")
    print("-" * 50)
    
    for continente in continentes:
        cantidad = 0
        poblacion_continente = 0
        superficie_continente = 0
        
        for pais in paises:
            if pais['continente'] == continente:
                cantidad = cantidad + 1
                poblacion_continente = poblacion_continente + pais['poblacion']
                superficie_continente = superficie_continente + pais['superficie']
        
        porcentaje = (cantidad / len(paises)) * 100
        
        print(f"{continente}:")
        print(f"  Paises: {cantidad} ({porcentaje:.1f}%)")
        print(f"  Poblacion total: {poblacion_continente:,}")
        print(f"  Superficie total: {superficie_continente:,} km2")
    
    # Mostrar resumen general
    print(f"\nRESUMEN GENERAL:")
    print("-" * 50)
    print(f"Total de paises: {len(paises)}")
    print(f"Total de continentes: {len(continentes)}")
    
    densidad_promedio = total_poblacion / total_superficie
    print(f"Densidad poblacional promedio: {densidad_promedio:.2f} hab/km2")
    
    print("="*60)

# ========================== FUNCIONES DE VISUALIZACIÓN ==========================

def mostrar_paises(lista_paises):
    """
    Muestra una lista de países en formato tabla profesional.
    
    Parámetros:
        lista_paises (list): Lista de diccionarios de países
    """
    if not lista_paises:
        print("📋 No hay países para mostrar.")
        return
    
    # Calcular anchos de columna dinámicamente
    max_nombre = max(len(pais['nombre']) for pais in lista_paises)
    max_continente = max(len(pais['continente']) for pais in lista_paises)
    
    # Asegurar anchos mínimos
    ancho_nombre = max(max_nombre, 15)
    ancho_poblacion = 15
    ancho_superficie = 15
    ancho_continente = max(max_continente, 15)
    ancho_densidad = 12
    
    ancho_total = ancho_nombre + ancho_poblacion + ancho_superficie + ancho_continente + ancho_densidad + 20
    
    # Encabezado
    print("\n" + "="*ancho_total)
    print(f"{'PAÍS':<{ancho_nombre}} │ {'POBLACIÓN':<{ancho_poblacion}} │ "
          f"{'SUPERFICIE':<{ancho_superficie}} │ {'CONTINENTE':<{ancho_continente}} │ "
          f"{'DENSIDAD':<{ancho_densidad}}")
    print(f"{'':<{ancho_nombre}} │ {'(habitantes)':<{ancho_poblacion}} │ "
          f"{'(km²)':<{ancho_superficie}} │ {'':<{ancho_continente}} │ "
          f"{'(hab/km²)':<{ancho_densidad}}")
    print("─"*ancho_total)
    
    # Datos de países
    for i, pais in enumerate(lista_paises, 1):
        densidad = pais['poblacion'] / pais['superficie'] if pais['superficie'] > 0 else 0
        
        print(f"{pais['nombre']:<{ancho_nombre}} │ "
              f"{pais['poblacion']:>{ancho_poblacion-1},} │ "
              f"{pais['superficie']:>{ancho_superficie-1},} │ "
              f"{pais['continente']:<{ancho_continente}} │ "
              f"{densidad:>{ancho_densidad-1}.1f}")
    
    print("="*ancho_total)
    print(f"Total de países mostrados: {len(lista_paises)}")

def mostrar_todos_los_paises():
    """
    Muestra todos los países cargados con opción de ordenamiento.
    """
    print("\n" + "="*50)
    print("TODOS LOS PAISES".center(50))
    print("="*50)
    
    if len(paises) == 0:
        print("No hay paises cargados en el sistema.")
        return
    
    print("Como desea ver los paises?")
    print("1. En el orden actual")
    print("2. Ordenados por nombre")
    print("3. Ordenados por poblacion (mayor a menor)")
    print("4. Ordenados por superficie (mayor a menor)")
    
    while True:
        opcion = input("Seleccione una opcion (1-4): ").strip()
        if opcion == '1' or opcion == '2' or opcion == '3' or opcion == '4':
            break
        print("Opcion invalida. Ingrese un numero del 1 al 4.")
    
    if opcion == '1':
        mostrar_paises(paises)
    elif opcion == '2':
        paises_ordenados = ordenar_paises_por_criterio(paises, 'nombre', True)
        print("Paises ordenados alfabeticamente:")
        mostrar_paises(paises_ordenados)
    elif opcion == '3':
        paises_ordenados = ordenar_paises_por_criterio(paises, 'poblacion', False)
        print("Paises ordenados por poblacion (mayor a menor):")
        mostrar_paises(paises_ordenados)
    elif opcion == '4':
        paises_ordenados = ordenar_paises_por_criterio(paises, 'superficie', False)
        print("Paises ordenados por superficie (mayor a menor):")
        mostrar_paises(paises_ordenados)

# ========================== MENÚ PRINCIPAL ==========================

def mostrar_menu():
    """
    Muestra el menú principal.
    """
    num_paises = len(paises)
    
    if len(paises) > 0:
        num_continentes = len(obtener_continentes_unicos())
    else:
        num_continentes = 0
    
    print("\n")
    print("╔" + "═"*70 + "╗")
    print("║" + " "*70 + "║")
    print("║" + "*** SISTEMA DE GESTION DE PAISES ***".center(70) + "║")
    print("║" + " "*70 + "║")
    print("╠" + "═"*70 + "╣")
    print("║" + f"  Estado: {num_paises} paises cargados | {num_continentes} continentes".ljust(70) + "║")
    print("╠" + "═"*70 + "╣")
    print("║" + " "*70 + "║")
    print("║" + "  >> GESTION DE DATOS".ljust(70) + "║")
    print("║" + "     ┌─────────────────────────────────────────────────────────┐".ljust(70) + "║")
    print("║" + "     │  [ 1]  Agregar pais manualmente                         │".ljust(70) + "║")
    print("║" + "     │  [ 2]  Actualizar datos de pais existente               │".ljust(70) + "║")
    print("║" + "     └─────────────────────────────────────────────────────────┘".ljust(70) + "║")
    print("║" + " "*70 + "║")
    print("║" + "  >> CONSULTAS Y BUSQUEDAS".ljust(70) + "║")
    print("║" + "     ┌─────────────────────────────────────────────────────────┐".ljust(70) + "║")
    print("║" + "     │  [ 3]  Buscar pais por nombre                           │".ljust(70) + "║")
    print("║" + "     │  [ 4]  Filtrar por continente                           │".ljust(70) + "║")
    print("║" + "     │  [ 5]  Filtrar por rango de poblacion                   │".ljust(70) + "║")
    print("║" + "     │  [ 6]  Filtrar por rango de superficie                  │".ljust(70) + "║")
    print("║" + "     └─────────────────────────────────────────────────────────┘".ljust(70) + "║")
    print("║" + " "*70 + "║")
    print("║" + "  >> ORDENAMIENTO".ljust(70) + "║")
    print("║" + "     ┌─────────────────────────────────────────────────────────┐".ljust(70) + "║")
    print("║" + "     │  [ 7]  Ordenar por nombre                               │".ljust(70) + "║")
    print("║" + "     │  [ 8]  Ordenar por poblacion                            │".ljust(70) + "║")
    print("║" + "     │  [ 9]  Ordenar por superficie                           │".ljust(70) + "║")
    print("║" + "     └─────────────────────────────────────────────────────────┘".ljust(70) + "║")
    print("║" + " "*70 + "║")
    print("║" + "  >> ANALISIS Y ESTADISTICAS".ljust(70) + "║")
    print("║" + "     ┌─────────────────────────────────────────────────────────┐".ljust(70) + "║")
    print("║" + "     │  [10]  Mostrar estadisticas generales                   │".ljust(70) + "║")
    print("║" + "     │  [11]  Mostrar todos los paises                         │".ljust(70) + "║")
    print("║" + "     └─────────────────────────────────────────────────────────┘".ljust(70) + "║")
    print("║" + " "*70 + "║")
    print("║" + "  >> SALIDA".ljust(70) + "║")
    print("║" + "     ┌─────────────────────────────────────────────────────────┐".ljust(70) + "║")
    print("║" + "     │  [ 0]  Salir del programa                               │".ljust(70) + "║")
    print("║" + "     └─────────────────────────────────────────────────────────┘".ljust(70) + "║")
    print("║" + " "*70 + "║")
    print("╚" + "═"*70 + "╝")

def opcion_cargar_csv():
    """
    Función auxiliar para la opción 1: Cargar países desde archivo CSV.
    Por defecto usa 'paises.csv' si el usuario presiona Enter sin ingresar nada.
    """
    global paises
    
    print("\n>> Cargando paises desde archivo CSV...")
    nombre_archivo = input("Ingrese el nombre del archivo CSV (Enter para 'paises.csv'): ").strip()
    
    # Si el usuario no ingresa nada, usar archivo por defecto
    if nombre_archivo == "":
        nombre_archivo = "paises.csv"
        print(f"Usando archivo por defecto: {nombre_archivo}")
    
    leer_csv(nombre_archivo)

def ejecutar_opcion_menu(opcion):
    """
    Ejecuta la opción seleccionada del menú principal.
    
    Retorna True para continuar, False para salir.
    """
    match opcion:
        case '1':
            agregar_pais()
        case '2':
            actualizar_pais()
        case '3':
            buscar_pais()
        case '4':
            filtrar_por_continente()
        case '5':
            filtrar_por_poblacion()
        case '6':
            filtrar_por_superficie()
        case '7':
            ordenar_por_nombre()
        case '8':
            ordenar_por_poblacion()
        case '9':
            ordenar_por_superficie()
        case '10':
            mostrar_estadisticas()
        case '11':
            mostrar_todos_los_paises()
        case '0':
            return False
        case _:
            print("\nError: Opcion invalida. Por favor, seleccione una opcion del 0 al 11.")
    
    return True

def mostrar_mensaje_bienvenida():
    """
    Muestra un mensaje de bienvenida al iniciar el programa.
    """
    print("\n")
    print("╔" + "═"*70 + "╗")
    print("║" + " "*70 + "║")
    print("║" + "*** SISTEMA DE GESTION DE PAISES ***".center(70) + "║")
    print("║" + " "*70 + "║")
    print("╠" + "═"*70 + "╣")
    print("║" + " "*70 + "║")
    print("║" + "  BIENVENIDO AL SISTEMA DE GESTION DE PAISES".ljust(70) + "║")
    print("║" + " "*70 + "║")
    print("║" + "  Este programa le permite:".ljust(70) + "║")
    print("║" + " "*70 + "║")
    print("║" + "    * Cargar y gestionar informacion de paises desde CSV".ljust(70) + "║")
    print("║" + "    * Realizar busquedas y filtros avanzados".ljust(70) + "║")
    print("║" + "    * Generar estadisticas y analisis detallados".ljust(70) + "║")
    print("║" + "    * Ordenar y visualizar datos de forma clara".ljust(70) + "║")
    print("║" + " "*70 + "║")
    print("╠" + "═"*70 + "╣")
    print("║" + " "*70 + "║")
    print("║" + "  Desarrollado para Programacion 1 - UTN".ljust(70) + "║")
    print("║" + "  Por: Aguero Maximiliano y Dario Frison".ljust(70) + "║")
    print("║" + " "*70 + "║")
    print("╚" + "═"*70 + "╝")
    print("\n")

def mostrar_mensaje_despedida():
    """
    Muestra un mensaje de despedida al salir del programa.
    """
    print("\n")
    print("╔" + "═"*70 + "╗")
    print("║" + " "*70 + "║")
    print("║" + "*** SALIENDO DEL SISTEMA ***".center(70) + "║")
    print("║" + " "*70 + "║")
    print("╠" + "═"*70 + "╣")
    print("║" + " "*70 + "║")
    print("║" + "  Sesion finalizada correctamente.".ljust(70) + "║")
    print("║" + f"  Paises procesados: {len(paises)}".ljust(70) + "║")
    
    if len(paises) > 0:
        continentes = obtener_continentes_unicos()
        print("║" + f"  Continentes trabajados: {len(continentes)}".ljust(70) + "║")
    
    print("║" + " "*70 + "║")
    print("║" + "  Gracias por usar el Sistema de Gestion de Paises!".ljust(70) + "║")
    print("║" + " "*70 + "║")
    print("╠" + "═"*70 + "╣")
    print("║" + " "*70 + "║")
    print("║" + "  Por: Aguero Maximiliano y Dario Frison".ljust(70) + "║")
    print("║" + "  Desarrollado para Programacion 1 - UTN".ljust(70) + "║")
    print("║" + " "*70 + "║")
    print("╚" + "═"*70 + "╝")
    print("\n")

def main():
    """
    Función principal que ejecuta el programa.
    Controla el flujo general: bienvenida -> menú -> operaciones -> despedida
    """
    # Mostrar mensaje de bienvenida al usuario
    mostrar_mensaje_bienvenida()
    
    # Cargar archivo CSV automáticamente al iniciar
    print("\n>> Cargando datos iniciales desde archivo CSV...")
    leer_csv("paises.csv")
    input("\n>> Presione Enter para continuar...")
    
    # Ciclo principal del programa
    continuar = True
    while continuar:
        mostrar_menu()
        
        # Solicitar opción
        opcion = input("\n>> Seleccione una opcion [0-11]: ").strip()
        
        # Ejecutar la opción elegida
        continuar = ejecutar_opcion_menu(opcion)
        
        # Pausa para que el usuario pueda leer los resultados
        if continuar:
            print("\n" + "─"*70)
            input(">> Presione Enter para continuar...")
    
    # Mostrar mensaje de despedida al salir
    mostrar_mensaje_despedida()

# ========================== EJECUCIÓN DEL PROGRAMA ==========================

if __name__ == "__main__":
    main()