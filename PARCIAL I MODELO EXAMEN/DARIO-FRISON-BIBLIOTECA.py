opciones_menu = [
    "1. Ingresar titulo (sin ejemplares)"
    "2. Ingresar ejemplares disponibles (sin titulo)",
    "3. Motrar catalogo de libros",
    "4. Consultar disponibilidad de un titulo especifico",
    "5. Listar agotados",
    "6. Agregar titulo (con ejemplares)"
    "7. Actualizar ejemplares (prestamo / devolucion)",
    "8. Ver catalogo completo",
    "9. Salir"
]
titulos = []
ejemplares = []

while True:
    print(" -- Menu Biblioteca --")
    for opcion in opciones_menu:
        print(opcion)

    seleccion = input("Seleccione una opcion: ")

    print("--------------------------------")

    if seleccion == "1":

        titulo = input("Ingresar titulo: ")
        while titulo in titulos or titulo == "":
            print(" ** ** **")
            print("El titulo ya existe o esta vacio")
            titulo = input("Ingrese nuevamente el titulo: ")
            print("** ** ** ")
        print(f"Titulo ingresado: {titulo}")
        titulos.append(titulo)
        posicion = titulo.index(titulo)
        # Aca no se uso append porque no se sabe la posicion del titulo en la lista
        ejemplares.insert(posicion, 0)

    elif seleccion == "2":

        if not titulos:
            print("No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares")
            continue
        
        # Listar titulos disponibles

        for i, titulo in enumerate(titulos):
            print(f"{i + 1}. {titulo}")

        posicion = int(input("Seleccione el numero de titulo para ingresar cantidad de ejemplares: ")) - 1

        # Validar que la posicion sea valida

        while posicion < 0 or posicion >= len(titulos):
            print("Posicion invalida, intente nuevamente")
            posicion = int(input("Seleccione el numero de titulo para ingresar cantidad de ejemplares: ")) - 1

        cantidad = int(input("Ingrese la cantidad de ejemplares: "))
        ejemplares[posicion] += cantidad
        print(f"Ejemplares disponibles actualmente para {titulos[posicion]}: {ejemplares[posicion]}")

    elif seleccion == "3":
        pass
    elif seleccion == "4":
        pass
    elif seleccion == "5":
        pass
    elif seleccion == "6":
        pass
    elif seleccion == "7":
        pass
    elif seleccion == "8":
        pass
    elif seleccion == "9":
        break
    else:
        print("Opcion no valida")
        