from menu_reproduccion import Menu


class Video:
    def __init__(self, titulo: str, formato: 'mp4', duracion: str, resolucion: int, velocidad_de_reproduccion: int, subtitulos: str):
        self.titulo = titulo
        self.formato = formato
        self.duracion = duracion
        self.resolucion = resolucion
        self.velocidad_de_reproduccion = velocidad_de_reproduccion
        self.subtitulos = subtitulos
        self.pausado = False
        self.menu = Menu()

    def imprime_datos_video(self):
        datos_pelicula = [self.titulo, self.duracion]
        for i in range(len(datos_pelicula)):
            print(datos_pelicula[i])