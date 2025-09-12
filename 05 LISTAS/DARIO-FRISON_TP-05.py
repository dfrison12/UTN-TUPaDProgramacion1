# TP 5 - Listas - Tecnicatura Universitaria en Programación
# Alumno: Dario Frison

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


# Ejecutar Ejericios
ejercicio_1()
ejercicio_2()