baul=[]

while True:
    print("1. Agregar artículo al baúl")
    print("2. Listar artículo del baúl")
    print("3. Borrar último artículo del baúl")
    print("4. Borrar un artículo específico")
    print("5. Salir")

    op=int(input("Ingrese la opción a realizar: "))

    if op==1:
        articulo=input("Ingrese el artículo a guardar: ")
        baul.append(articulo)
    elif op==2:
        print(baul)
    elif op==3:
        res=input("Si deseas borrar el último articulo de la lista escribe s de lo contrario n: ")
        if res=="s" or res=="S":
            baul.pop()
            print("El artículo ha sido borrado")
        else:
            print("ok puedes seguir")
            continue
    elif op==4:
        for i,a in enumerate(baul):
            print("Articulo No. ",i,":",a)
        ab=int(input("Ingrese la posición del artículo que desea borrar: "))
        del baul[ab]
        print("El artículo ha sido borrado")
    elif op==5:
        break
    else:
        print("Opción es invalida")
        break
