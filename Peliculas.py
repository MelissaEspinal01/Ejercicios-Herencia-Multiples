from Contenido import Contenido
class Pelicula:
    def __init__(self, Pelicula1, Pelicula2, Pelicula3):
        self.Pelicula1 = Pelicula1
        self.Pelicula2 = Pelicula2
        self.Pelicula3 = Pelicula3
        self.contenido = Contenido()

    def mostrar_peliculas(self):
        return "La pelicula {} se encuentra en la categoria {}, La pelicula {} se encuentra en la categoria {}, La pelicula {} se encuentra en la categoria {}".format(self.Pelicula1, self.contenido.Categoria1, self.Pelicula2, self.contenido.Categoria2, self.Pelicula3, self.contenido.Categoria3)
