GENERO = ["Ficcion","No ficcion","Ciencia"]


def Registrar_libro(Libros):
    while True:
        Titulo = input("Ingrese el titulo del libro: ").capitalize()
        Autor = input("Ingrese el nombre del autor: ").capitalize()
        Genero = input("Ingrese el genero del libro(Ficcion/No ficcion/Ciencia): ").capitalize()
        while Genero not in GENERO:
            print("Este genero no esta")
            Genero = input("Ingrese el genero del libro: ").capitalize()
        Precio = 5000
        break
    
    Cantidad_venta = 1 
    Precio_unidad = Precio
    Precio_total = Precio * Cantidad_venta 



    Libros.append({ 
        "Titulo":Titulo,
        "Autor":Autor,
        "Genero":Genero,
        "Precio":Precio,
        "Cantida_venta":Cantidad_venta,
        "Precio_unidad":Precio_unidad,
        "Precio_total":Precio_total
    })

def Lista_libros(Libros):
    for Libro in Libros:
        print(Libro)



def Registrar_ventas(Libros,Titulo):
    Registrar = False
    for Libro in Libros:
        if Libro["Titulo"] == Titulo:
            print(f"Titulo: {Libro["Titulo"]},Cantidad vendidos: {Libro["Cantida_venta"]},Precio total: {Libro["Precio_total"]}")
        Registrar = True
    while not Registrar:
        print("Este libro no esta registrado")




def Imprimir_lista(Libros):
    Seleccionar_genero = input("Ingrese el genero que desea imprimr o aprete ENTER para imprimir todos los generos: ").capitalize()
    if Seleccionar_genero == "":
        Guardar_libros = Libros
        Imprimir_libros ="Imprimir_libros.txt"
    elif Seleccionar_genero == GENERO:
        Guardar_libros = []
        for Libro in Libros:
            if Libro["Genero"] == Seleccionar_genero:
                Guardar_libros = Libros
                Imprimir_libros = f"Imprimir_genero_{Seleccionar_genero}.txt"

    with open(Imprimir_libros, "w") as archivo:
        for Libro in Guardar_libros:
            archivo.write(f"\nTitulo: {Libro["Titulo"]}\n")
            archivo.write(f"Autor: {Libro["Autor"]}\n")
            archivo.write(f"Genero: {Libro["Genero"]}\n")
            archivo.write(f"Precio: {Libro["Precio"]}\n")

    