class Perfil:
    def __init__(self, nombre: str, foto=None):
        self.nombre = nombre
        self.foto = foto
        self.random_sp = []

    def cambiar_nombre(self, nuevoNombre):
        self.nombre = nuevoNombre

perfiles_lista = []
p1 = Perfil("Gaby")
perfiles_lista.append(p1)
p2 = Perfil("Roldan")
perfiles_lista.append(p2)
p3 = Perfil("Agraz")
perfiles_lista.append(p3)

p4 = Perfil("Luis")
perfiles_lista.append(p4)
p5 = Perfil("Roberto")
perfiles_lista.append(p5)
p6 = Perfil("Juan")
perfiles_lista.append(p6)