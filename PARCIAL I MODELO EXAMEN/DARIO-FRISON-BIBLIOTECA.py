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

libros = []
ejemplares = []

while True:
    print(" -- Menu Biblioteca --")
    for opcion in opciones_menu:
        print(opcion)

    seleccion = input("Seleccione una opcion: ")

    print("--------------------------------")

    if seleccion == "1":

        titulo = input("Ingresar titulo: ")
        while titulo in libros or titulo == "":
            print(" ** ** **")
            print("El titulo ya existe o esta vacio")
            titulo = input("Ingrese nuevamente el titulo: ")
            print("** ** ** ")
        print(f"Titulo ingresado: {titulo}")
        libros.append(titulo)
        posicion = titulo.index(titulo)
        # Aca no se uso append porque no se sabe la posicion del titulo en la lista
        ejemplares.insert(posicion, 0)

    elif seleccion == "2":
        pass
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
        