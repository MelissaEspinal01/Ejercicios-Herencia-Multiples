from Peliculas import Pelicula

class Cliente:
    def __init__(self):
        self.peliculas_disponibles = Pelicula("Avengers", "Toy Story", "The Exorcist")

    def mostrar_peliculas(self):
        print("Las peliculas disponibles son:")
        print(self.peliculas_disponibles.mostrar_peliculas())

    def elegir_pelicula(self):
        pelicula_elegida = input("Ingrese el nombre de la pelicula que desea ver: ")
        if pelicula_elegida == self.peliculas_disponibles.Pelicula1:
            print("Usted ha elegido la pelicula '{}' de la categoria {}".format(self.peliculas_disponibles.Pelicula1, self.peliculas_disponibles.contenido.Categoria1))
        elif pelicula_elegida == self.peliculas_disponibles.Pelicula2:
            print("Usted ha elegido la pelicula '{}' de la categoria {}".format(self.peliculas_disponibles.Pelicula2, self.peliculas_disponibles.contenido.Categoria2))
        elif pelicula_elegida == self.peliculas_disponibles.Pelicula3:
            print("Usted ha elegido la pelicula '{}' de la categoria {}".format(self.peliculas_disponibles.Pelicula3, self.peliculas_disponibles.contenido.Categoria3))
        else:
            print("La pelicula ingresada no se encuentra disponible")

cliente = Cliente()
cliente.mostrar_peliculas()
cliente.elegir_pelicula()

