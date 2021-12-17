import sys


class Menu:
    def __init__(self):
        self.pausado = False
        self.adelantado = False
        self.retrocediendo = False
        self.idioma = False
        self.salida = False
        self.choices = {
            '1': self.reproducir,
            '2': self.pausa,
            '3': self.adelantar,
            '4': self.retroceder,
            '5': self.cambiar_idioma,
            '6': self.subtitulos,
            '7': self.salir,
        }

    def display_menu(self):
        print(
                """
VIDEO MENU 
1. Reproducir
2. Pausa
3. Adelantar
4. Retroceder
5. Cambiar de Idioma
6. Subtitulos
7. Salir
""")

    def run(self):
        """Muestra el menu y sus opciones"""
        while True:
            self.display_menu()
            choice = input("Pulsa el numero de tu eleccion para esocger una opcion ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} No es una opcion valida".format(choice))



    def reproducir(self):
        """Reproduce un video"""
        print("Tu video se esta reproduciendo")


    def pausa(self):
        """Si presionas 'p' se pausa el reproductor"""
        p = input("Presiona 'p ' para pausar o reanudar el video\n")
        if p == 'p':
            if self.pausado:
                print("La pelicula se reanuda")
                self.pausado = False

            else:
                print("La pelicula se pauso")
                self.pausado = True


    def adelantar(self):
        '''Al poner la primera vez A se adelanta 5 segundos, si vuelves a picar A se adelanta 10 seg'''
        a = input('Presiona "a" para adelantar el video 5 o 10 segundos: ')
        if a == 'a':
            if self.adelantado:
                print("La pelicula se adelanto 10 segundos")
                self.adelantado = False
            else:
                print("La pelicula se adelanto 5 segundos")
                self.adelantado = True

    def retroceder(self):
        '''Al poner la primera vez R se retrasa el video, si vuelves a picar A se retrasa 10 seg'''
        r = input('Presiona "r" para retrasar 5 segundos el video: ')
        if r == 'r':
            if self.retrocediendo:
                print("La pelicula se retrocedio 10 segundos")
                self.retrocediendo = False
            else:
                print("La pelicula se retrocedio 5 seg")
                self.retrocediendo = True

    def cambiar_idioma(self):
        i = input('1: Spanish \n2: English\n')
        if i != '1':
            print("Language in English")
            self.idioma = True
        else:
            print("Lenguaje en Español")
            self.idioma = True

    def subtitulos(self):
        s = input('1: On \n2: Off\n')
        if s != '1':
            print("Subtitles OFF")
            self.idioma = True
        else:
            print("Subtitles ON")
            self.idioma = True

    def salir(self):
        saliendo = input('Seguro que quieres salir del video? (si/no) ')
        saliendo_2 = saliendo.lower()
        if saliendo_2 != 'si':
            print("Video reproduciendose")
            self.salida = True
        else:
            print('Saliendo de la reproducción')
            sys.exit(0)

if __name__ == '__main__':
    v=Menu()
    v.run()