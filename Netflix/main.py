from perfil import Perfil
from log_In import Log_In
from usuario import Usuario


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

usuario1 = Usuario(correo="abc@gmail.com", password="123")
usuario1.perfiles.append(p1)
usuario1.perfiles.append(p2)
usuario1.perfiles.append(p3)

usuario2 = Usuario(correo="itsme@hotmail.com", password="blah")
usuario2.perfiles.append(p4)
usuario2.perfiles.append(p5)
usuario2.perfiles.append(p6)

if __name__ == '__main__':
    p = Log_In(correo='abc@.com', password='123', perfiles_mostrar=perfiles_lista)
    usuario = p.iniciar_sesion()




