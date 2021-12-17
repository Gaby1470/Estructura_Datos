from video import Video


class Series(Video):
    def __init__(self, capitulos: str, temporadas: str, actores: str, **kwargs):
        super().__init__(**kwargs)
        self.capitulos = capitulos
        self.temporadas = temporadas
        self.actores = actores

    def imprime_datos(self):
        super().imprime_datos_video()
        datos_pelicula = [ self.actores, self.temporadas, self.capitulos]
        for i in range(len(datos_pelicula)):
            print(datos_pelicula[i])

