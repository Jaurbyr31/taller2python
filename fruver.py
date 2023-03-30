fruver = {}
while True:
    print("Fruver Supermercados Noé")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    
    opcion = int(input("¿Qué opción deseas realizar?: "))
    if opcion == 1:
        nombre = input("Nombre de la fruta: ")     
        if nombre in fruver:
            print("%s ya existe la fruta registrada y su precio es %s" % (nombre,fruver[nombre]))
            opcion = input("Pulsa 's' si quieres modificar el precio. Otra tecla para continuar.")
            if opcion == "s":
                precio = input("Dame el nuevo precio de la fruta: ")
                fruver[nombre]=precio
        else:
            precio = int(input("Dame el precio de la fruta: "))
            fruver[nombre]=precio
    elif opcion == 2:
        texto = input("Nombre de la fruta a buscar:")
        print("Se encontraron los siguientes resultados:")    
        for nombre, precio in fruver.items():
            if nombre.startswith(texto):
                print("El precio de la fruta ingresada", nombre, "es", fruver[nombre])
    elif opcion == 3:
        nombre = input("Nombre de la fruta a eliminar:")    
        if nombre in fruver:
            opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar.")
            if opcion == "s":
                del fruver[nombre]
        else:
            print("No existe la fruta indicada")
    elif opcion == 4:
        for nombre, precio in fruver.items():
            print(nombre,"->",precio)
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")
