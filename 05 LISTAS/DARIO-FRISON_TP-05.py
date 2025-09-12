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

# Ejecutar Ejericios
ejercicio_1()
ejercicio_2()
ejercicio_3()
ejercicio_4()
ejercicio_5()
ejercicio_6()