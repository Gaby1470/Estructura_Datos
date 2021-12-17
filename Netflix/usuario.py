from netflix_Console import Menu_Users
from perfil import Perfil


class Usuario:
    """Log In """

    def __init__(self, correo, password, menu=None):
        self.correo = correo
        self.password = password
        self.menu = menu
        self.perfiles = []


usuario1 = Usuario(correo="abc@gmail.com", password="123")
usuario2 = Usuario(correo="itsme@hotmail.com", password="blah")
usuario3 = Usuario(correo='david@gmail.com', password='roldan')
usuario4 = Usuario(correo='manuel@yahoo.com', password='sup')

if __name__ == '__main__':
    perfiles = []
    p1 = Perfil("Gaby")
    perfiles.append(p1)
    p1 = Perfil("Roldan")
    perfiles.append(p1)
    p1 = Perfil("Agraz")
    perfiles.append(p1)
    m = Menu_Users(perfiles)
    u = Usuario('abc@hotm.com', 1, m)
    u.menu.run()