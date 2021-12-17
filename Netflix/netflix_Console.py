from perfil import Perfil, perfiles_lista
from favoritos import random_sp
from menu_reproduccion import Menu
import random

for i in range (3):
    random.choice(perfiles_lista)

class Menu_Users:
    """Muestra los perfiles que se tienen"""

    def __init__(self, perfiles_lista: list):
        self.perfiles_lista = perfiles_lista
        self.choices = {
            "1": self.perfil_1,
            "2": self.perfil_2,
            "3": self.perfil_3,
            "4": self.agregarPerfil,
            "5": self.BorrarPerfil,
        }

    def display_menu(self):
        print(
            f"""
CHOOSE A PROFILE
1. {self.perfiles_lista[0].nombre}
2. {self.perfiles_lista[1].nombre}
3. {self.perfiles_lista[2].nombre} 
4. Agregar Perfil
5. Eliminar Perfil
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


    def perfil_1(self):

        for i in range(len(random_sp)):
            print(str(i + 1) + ".", random_sp[i].titulo)
        cual = int(input("Que quieres ver:\n "))
        random_sp[cual-1].imprime_datos()
        print(Menu().run())


    def perfil_2(self):
        for i in range(len(random_sp)):
            print(str(i + 1) + ".", random_sp[i].titulo)
        cual = int(input("Que quieres ver:\n "))
        random_sp[cual - 1].imprime_datos()
        print(Menu().run())

    def perfil_3(self):
        for i in range (len(random_sp)):
            print(str(i + 1) + ".", random_sp[i].titulo)
        cual = int(input("Que quieres ver:\n "))
        random_sp[cual - 1].imprime_datos()
        print(Menu().run())

    def agregarPerfil(self):
        for n, u in enumerate(self.perfiles_lista):
            print(str(n + 1) + ".", u.nombre)
        cual = int(input("Ingresa cual perfil quieres cambiar: "))
        nombre = input("Por favor, ingresa tu nombre ")
        self.perfiles_lista[cual - 1].cambiar_nombre(nombre)

    def BorrarPerfil(self):
        for n, u in enumerate(self.perfiles_lista):
            print(str(n + 1) + ".", u.nombre)
        cual = int(input("Ingresa cual perfil quieres cambiar: "))
        self.perfiles_lista[cual - 1].cambiar_nombre("Disponible")


if __name__ == '__main__':
    perfiles = []
    p1 = Perfil("Gaby")
    perfiles.append(p1)
    p1 = Perfil("Roldan")
    perfiles.append(p1)
    p1 = Perfil("Agraz")
    perfiles.append(p1)
    u = Menu_Users(perfiles)
    u.run()