import Funcion as fn

Libros = []

while True:
    print("Menu de libreria")
    print("\n1)Registrar libro\n2)Listar libro\n3)Registrar ventas\n4)Imprimir ventas\n5)Salir")

    opcion = int(input("Ingrese una opcion"))

    if opcion == 1:
        fn.Registrar_libro(Libros)
    elif opcion == 2:
        fn.Lista_libros(Libros)
    elif opcion == 3:
        Titulo = input("Ingrese el titulo del libros que quiere registrar: ").capitalize()
        fn.Registrar_ventas(Libros,Titulo)
    elif opcion == 4:
        fn.Imprimir_lista(Libros)
    elif opcion == 5:
        print("Gracias por visitar nuestra tienda")
        break
    else:
        print("Ingrese una opcion valida")      

