# TP 5 - Listas - Tecnicatura Universitaria en Programación
# Alumno: Dario Frison

import random

# Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.
def ejercicio_1():
    print("Ejercicio 1")

    CANTIDAD = 10
    notas = []

    for i in range(CANTIDAD):
        nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
        if nota < 0 or nota > 10:
            print("La nota debe estar entre 0 y 10")
            return
        notas.append(nota)


    print("Notas ingresadas:")
    for i in range(CANTIDAD):
        print(f"Estudiante {i + 1}: {notas[i]}")

    suma = 0.0
    mayor = notas[0]
    menor = notas[0]

    for nota in notas:
        suma += nota
        if nota > mayor:
            mayor = nota
        if nota < menor:
            menor = nota

    promedio = suma / CANTIDAD

    print(f"Promedio: {promedio}")
    print(f"Nota más alta: {mayor}")
    print(f"Nota más baja: {menor}")

# Ejercicio 2: Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
def ejercicio_2():
    print("Ejercicio 2 - Listas de productos")

    CANTIDAD = 5
    productos = []

    for i in range(CANTIDAD):
        nombre = input(f"Ingrese el nombre del producto {i + 1}: ")
        productos.append(nombre)

    ordenados = sorted(productos, key=str.lower)

    print("Lista de productos: ")
    for i in range(len(ordenados)):
        print(f"{i + 1}: {ordenados[i]}")

    a_eliminar = input("Ingrese el producto que desea eliminar: ")
    
    
    
    if a_eliminar in productos:
        productos.remove(a_eliminar)
    else:
        print("El producto no se encontró en la lista.")

    print("Lista actualizada de productos:")

    if len(productos) == 0:
        print("La lista está vacía.")
    else:
        for i in range(len(productos)):
            print(f"{i + 1}. {productos[i]}")

# Ejercicio 3: Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.
def ejercicio_3():
    print("Ejercicio 3")

    CANTIDAD = 15
    numeros = []
    pares = []
    impares = []

    for i in range(CANTIDAD):
        numeros.append(random.randint(1, 100))
        if numeros[i] % 2 == 0:
            pares.append(numeros[i])
        else:
            impares.append(numeros[i])

    print(f"Numeros: {numeros}")
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
    print(f"Cantidad de numeros: {len(numeros)}")
    print(f"Cantidad de pares: {len(pares)}")
    print(f"Cantidad de impares: {len(impares)}")

# Ejercicio 4: Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.
def ejercicio_4():
    print("Ejercicio 4")
    
    datos_del_ejericio = [1, 3, 5, 3, 7, 1, 9, 5, 3]
    datos_sin_repetir = []

    for x in datos_del_ejericio:
        if x not in datos_sin_repetir:
            datos_sin_repetir.append(x)

    print("Lista original: ")
    for i in range(len(datos_del_ejericio)):
        print(f"{datos_del_ejericio[i]}", end=" ")

    print("\nLista sin repetidos:")
    for i in range(len(datos_sin_repetir)):
        print(f"{datos_sin_repetir[i]}", end=" ")

# Ejercicio 5: Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.
def ejercicio_5():
    print("Ejercicio 5")
    
    estudiantes = ["Juan", "Maria", "Pedro", "Ana", "Luis", "Carlos", "Lucas", "Martin"]

    print("Lista de estudiantes: ")
    for i in range(len(estudiantes)):
        print(f"{i + 1}. {estudiantes[i]}")

    opcion = input("Ingrese la opcion que desea realizar (1 para agregar un nuevo estudiante o 2 para eliminar uno de la lista): ")

    if opcion == "1":

        nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
        estudiantes.append(nuevo_estudiante)
        print("Estudiante agregado correctamente")

    elif opcion == "2":
        
        estudiante_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
        i = 0
        estudiante_encontrado = ''
        
        while i < len(estudiantes) and estudiante_encontrado == '':
            if estudiantes[i].lower() == estudiante_a_eliminar.lower():
                estudiante_encontrado = estudiantes[i]
            i += 1
        
        if estudiante_encontrado != '':
            estudiantes.remove(estudiante_encontrado)
            print("Estudiante eliminado correctamente")
        else:
            print("Estudiante no encontrado en la lista")
    else:
        print("Ingresa una opcion valida")
    

    print("Lista final de estudiantes:")
    for i in range(len(estudiantes)):
        print(f"{i + 1}. {estudiantes[i]}")

        
# Ejercicio 6: Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).
 
def ejercicio_6():
    print("Ejercicio 6")

    numeros = [4, 8, 2, 9, 5, 1, 7]
    cantidad = len(numeros)

    print("Lista original:")

    for i in range(cantidad):
        print(f"posicion {i}: {numeros[i]}")

    ultimo = numeros[-1]
    for i in range(cantidad - 1, 0, -1):
        numeros[i] = numeros[i - 1]
    numeros[0] = ultimo

    print("Lista rotada a la derecha (1 posición):")

    for i in range(cantidad):
        print(f"posicion {i}: {numeros[i]}")

# Ejercicio 7: Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

def ejercicio_7():
    print("Ejercicio 7")

    matriz = [[25, 32], [24, 31], [23, 27], [26, 29], [20, 28], [24, 27], [23, 30]]

    suma_minima = 0
    suma_maxima = 0
    mayor_amplitud = 0
    dia_mayor_amplitud = 0


    for i in range(len(matriz)):

        temp_minima = matriz[i][0]
        temp_maxima = matriz[i][1]

        print(f"Dia {i + 1}: Mínima: {temp_minima}, Máxima: {temp_maxima}")

        suma_minima += temp_minima
        suma_maxima += temp_maxima

        if temp_maxima - temp_minima > mayor_amplitud:
            mayor_amplitud = temp_maxima - temp_minima
            dia_mayor_amplitud = i + 1
    

    print(f"Promedio de las mínimas: {suma_minima / len(matriz)}")
    print(f"Promedio de las máximas: {suma_maxima / len(matriz)}")
    print(f"Dia con mayor amplitud térmica: {dia_mayor_amplitud}")
    print(f"Mayor amplitud térmica: {mayor_amplitud}")

# Ejercicio 8: Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

def ejercicio_8():
    print("Ejercicio 8")
    
    matriz_notas = [[9, 9, 9], [6, 6, 6], [9, 7, 8], [7, 8, 9], [8, 7, 9]]
    cantidad_estudiantes = len(matriz_notas)
    cantidad_materias = len(matriz_notas[0])

    for i in range(cantidad_estudiantes):
        suma_notas_estudiante = 0

        for j in range(cantidad_materias):
            suma_notas_estudiante += matriz_notas[i][j]
        
        promedio_estudiante = suma_notas_estudiante / cantidad_materias
        print(f"Promedio del estudiante {i + 1}: {promedio_estudiante}")
    
    for j in range(cantidad_materias):
        suma_notas_materia = 0
        for i in range(cantidad_estudiantes):
            suma_notas_materia += matriz_notas[i][j]

        promedio_materia = suma_notas_materia / cantidad_estudiantes
        print(f"Promedio de la materia {j + 1}: {promedio_materia}")
    
# Ejercicio 9: Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.
def ejercicio_9():
    print("Ejercicio 9")
    
    tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    
    def mostrar_tablero():
        print("\nTablero actual:")
        for i in range(3):
            for j in range(3):
                print(tablero[i][j], end=" ")
            print() 
        print()
    
    mostrar_tablero()
    
    turnos_jugados = 0
    
    while turnos_jugados < 9:
        if turnos_jugados % 2 == 0:
            ficha_jugador = "X"
            print("Turno del jugador X (Ingrese 0 para salir)")
        else:
            ficha_jugador = "O"
            print("Turno del jugador O (Ingrese 0 para salir)")
        
        fila = int(input("Ingrese la fila (1, 2 o 3): "))
        if fila < 1 or fila > 3:
            if fila == 0:
                break
            print("- La fila debe ser 1, 2 o 3")
            continue

        columna = int(input("Ingrese la columna (1, 2 o 3): "))
        if columna < 1 or columna > 3:
            if columna == 0:
                break
            print("-La columna debe ser 1, 2 o 3")
            continue
        
        if tablero[fila - 1][columna - 1] != "-":
            print("- Esa casilla ya está ocupada")
        else:
            tablero[fila - 1][columna - 1] = ficha_jugador
            turnos_jugados += 1
        
        mostrar_tablero()
    
    print("¡Juego terminado!")

# Ejercicio 10: Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana
def ejercicio_10():
    print("Ejercicio 10")
    
    matriz_ventas = [[2000, 340, 100, 250, 150, 300, 660], [150, 200, 1200, 280, 180, 250, 190], [220, 300, 150, 280, 190, 260, 210], [18980, 250, 130, 270, 170, 240, 200]]
    cantidad_productos = len(matriz_ventas)
    cantidad_dias = len(matriz_ventas[0])
    totales_productos = []
    
    for i in range(cantidad_productos):
        total_ventas_producto = 0
        mayor_venta_producto = 0
        posicion_mayor_venta_producto = -1


        for j in range(cantidad_dias):
            producto_actual = matriz_ventas[i][j]
            total_ventas_producto += producto_actual

            if producto_actual > mayor_venta_producto:
                mayor_venta_producto = producto_actual
                posicion_mayor_venta_producto = j + 1


        totales_productos.append(total_ventas_producto)

        print(f"Total vendido del producto {i + 1}: {total_ventas_producto}")
        print(f"Dia con mayor venta del producto {i + 1}: Dia {posicion_mayor_venta_producto} con {mayor_venta_producto} ventas")

    producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
    print(f"Producto mas vendido: {producto_mas_vendido}")


# Ejecutar Ejericios
ejercicio_1()
ejercicio_2()
ejercicio_3()
ejercicio_4()
ejercicio_5()
ejercicio_6()
ejercicio_7()
ejercicio_8()
ejercicio_9()
ejercicio_10()