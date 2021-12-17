from video import Video


class Peliculas(Video):
    def __init__(self, director: str, actores: str, clasificacion: str, genero: str, year: int,
                 descripcion=None, **kwargs):
        super().__init__(**kwargs)
        self.director = director
        self.actores = actores
        self.clasificacion = clasificacion
        self.genero = genero
        self.year = year
        self.descripcion = descripcion

    def imprime_datos(self):
        super().imprime_datos_video()
        datos_pelicula = [self.director, self.actores, self.clasificacion, self.genero, self.year]
        for i in range(len(datos_pelicula)):
            print(datos_pelicula[i])
