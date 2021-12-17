from usuario import Usuario, usuario1, usuario2, usuario3, usuario4
from netflix_Console import Menu_Users
from perfil import Perfil

perfiles_lista = []
p1 = Perfil("Gaby")
perfiles_lista.append(p1)
p2 = Perfil("Roldan")
perfiles_lista.append(p2)
p3 = Perfil("Agraz")
perfiles_lista.append(p3)


class Log_In(Usuario):
    def __init__(self, perfiles_mostrar : list, **kwargs):
        super().__init__(**kwargs)
        self.perfiles_mostrar = perfiles_mostrar

    def iniciar_sesion(self):
        """Ingresa el correo y contra, si el correo no tiene un @ o .com le pide volver a ingresar datos"""
        while True:
            print("----------------N E T L F I X---------------- \n")
            correo = input("Ingresa tu correo: ")
            password = input("Ingresa tu contraseña: ")
            if ("@" in correo) and ('.com' in correo):
                if (usuario1.correo == correo and usuario1.password == password):
                    print('\nINICIANDO...\n')
                    print("Correo ingresado correctamente\n")
                    Menu_Users(perfiles_lista).run()
                elif (usuario2.correo == correo and usuario2.password == password):
                    print('\nINICIANDO...\n')
                    print("Correo ingresado correctamente\n")
                    Menu_Users(perfiles_lista).run()
                elif(usuario3.correo == correo and usuario3.password == password):
                    print('\nINICIANDO...\n')
                    print("Correo ingresado correctamente\n")
                    Menu_Users(perfiles_lista).run()
                elif (usuario4.correo == correo and usuario4.password == password):
                    print('\nINICIANDO...\n')
                    print("Correo ingresado correctamente\n")
                    Menu_Users(perfiles_lista).run()
                else:
                    print('Datos incorrectos \n')


if __name__ == '__main__':
    p = Log_In(correo='abc@.com', password='123', perfiles_mostrar=perfiles_lista)
    p.iniciar_sesion()


