from guizero import App, Text, PushButton, Box, Window, TextBox
import random


# -------------------------DESABILITAR BOTON-------------------------------
def DISABLE(button):
    button.disable()


# -------------------------CERRAR VENTANA AL PRESIONAR BOTON-------------
def CLOSE(window):
    window.destroy()


# -------------------------CONTADOR-----------------------------------------
def CONTADOR(puntos):
    global botones_presionados
    global contador
    contador = contador + int(puntos)
    CONT.value = "Puntos: " + str(contador)

    botones_presionados += 1

    if botones_presionados == 30:
        window = Window(app, "YOU DONE BISH", bg="black", height=400, width=500)
        text = Text(window, "TE LLEVASTE " ,size=30, color="yellow")
        text = Text(window, str(contador),size=45, color="white" )
        text = Text(window," PUNTOS \n",size=30, color="yellow")
        Button = PushButton(window, text="CLICK ME TO QUIT LMAO", command=SALIR, width=25, height=3)
        Button.text_color="white"
        Button.bg="#030749"




# -------------------------SALIR DEL PRGRAMA-----------------------------------------
def SALIR():
    app.destroy()

# ------------------------FUNCIONES DE CATEGORIA 1------------------------#
def CATEGORIA_1(x):
    CAT_1 = Box(GAME_BOARD, layout="auto", grid=[x, 0])

    Titulo = Text(CAT_1, text=" Los compas del salón  ", color="yellow")

    B100 = PushButton(CAT_1, text="100", command=lambda: [PREGUNTAS_RANDOM_CAT1(100), DISABLE(B100)], width=6, height=1)
    B100.text_color = "white"
    B100.text_size = 17

    B200 = PushButton(CAT_1, text="200", command=lambda: [PREGUNTAS_RANDOM_CAT1(200), DISABLE(B200)], width=6, height=1)
    B200.text_color = "white"
    B200.text_size = 17

    B300 = PushButton(CAT_1, text="300", command=lambda: [PREGUNTAS_RANDOM_CAT1(300), DISABLE(B300)], width=6, height=1)
    B300.text_color = "white"
    B300.text_size = 17

    B400 = PushButton(CAT_1, text="400", command=lambda: [PREGUNTAS_RANDOM_CAT1(400), DISABLE(B400)], width=6, height=1)
    B400.text_color = "white"
    B400.text_size = 17

    B500 = PushButton(CAT_1, text="500", command=lambda: [PREGUNTAS_RANDOM_CAT1(500), DISABLE(B500)], width=6, height=1)
    B500.text_color = "white"
    B500.text_size = 17


def PREGUNTA_1_CAT1(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿De dónde es Daniel Agraz? \n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Sonora", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Chihuahua", width=13, height=2, command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Guadalajara", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_2_CAT1(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Qué otra carrera estudio Axel?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Ingeniería Civil", width=25, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Negocios", width=25, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Ingeniería en producción musical", width=25, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_3_CAT1(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=600, height=400)

    P = Text(window, text="¿Quién tiene como mascota una tortuga?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Carlos", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Juan", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Michelle", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_4_CAT1(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Cuánto mide Stephanie?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="1.76", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="1.74", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="1.80", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_5_CAT1(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Cuál es la comida favorita de Matsu?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Tacos", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Katsudon", width=14, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Sushi", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_6_CAT1(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Cuál es la comida favorita de Samuel?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Torta Ahogada", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Enchiladas", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Tacos de birria", width=15, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_7_CAT1(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿A dónde ha viajado Carlos?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Argentina", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Brasil", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Alemania", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_8_CAT1(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Qué deporte practica Michelle?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Fútbol americano", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Flag", width=14, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Fútbol soccer", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_9_CAT1(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Quién es fan de Marvel?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Manuel", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Melany", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Ivannia", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_10_CAT1(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=600, height=400)

    P = Text(window, text="¿Quién es conocido por su foto en Zoom como Stitch?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Juan", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Gustavo", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Roldan", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTAS_RANDOM_CAT1(case):
    preguntas_random_cat1

    if case == 100:
        return preguntas_random_cat1[0](case)
    elif case == 200:
        return preguntas_random_cat1[1](case)
    elif case == 300:
        return preguntas_random_cat1[2](case)
    elif case == 400:
        return preguntas_random_cat1[3](case)
    else:
        return preguntas_random_cat1[4](case)


# ------------------------FUNCIONES DE CATEGORIA 2------------------------#
def CATEGORIA_2(x):
    CAT_2 = Box(GAME_BOARD, layout="auto", grid=[x, 0])

    Titulo = Text(CAT_2, text="     ICC Universal     ", color="yellow")

    B100 = PushButton(CAT_2, text="100", command=lambda: [PREGUNTAS_RANDOM_CAT2(100), DISABLE(B100)], width=6, height=1)
    B100.text_color = "white"
    B100.text_size = 17

    B200 = PushButton(CAT_2, text="200", command=lambda: [PREGUNTAS_RANDOM_CAT2(200), DISABLE(B200)], width=6, height=1)
    B200.text_color = "white"
    B200.text_size = 17

    B300 = PushButton(CAT_2, text="300", command=lambda: [PREGUNTAS_RANDOM_CAT2(300), DISABLE(B300)], width=6, height=1)
    B300.text_color = "white"
    B300.text_size = 17

    B400 = PushButton(CAT_2, text="400", command=lambda: [PREGUNTAS_RANDOM_CAT2(400), DISABLE(B400)], width=6, height=1)
    B400.text_color = "white"
    B400.text_size = 17

    B500 = PushButton(CAT_2, text="500", command=lambda: [PREGUNTAS_RANDOM_CAT2(500), DISABLE(B500)], width=6, height=1)
    B500.text_color = "white"
    B500.text_size = 17


def PREGUNTA_1_CAT2(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Quien desarrolló el álgebra booleana?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="John Von Neumann", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="George Boole", width=15, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Paul Allen", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_2_CAT2(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=700, height=400)

    P = Text(window, text="¿Quién es considerada la madre de la programación informática?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Grace Hopper", width=18, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Barbara Liskov", width=18, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text=" Lady Ada Lovelace", width=18, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_3_CAT2(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=550)

    P = Text(window, text="¿Quién fue el compañero de Steve Jobs?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text=" Linus Torvalds", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Paul Allen", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text=" Steve Wozniak", width=15, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_4_CAT2(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=650)

    P = Text(window, text="Es conocido como el abuelo de las ciencias computacionales")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="y se le acuña el término <<algoritmo>>\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Al-Khwarizmi", width=15, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Blaise Pascal", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Alan Turing", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_5_CAT2(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=550)

    P = Text(window, text="¿Quién participó en el Proyecto Manhattan?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Dennis Ritchie", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="John Von Neumann ", width=15, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Charles Babbage", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_6_CAT2(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=600)

    P = Text(window, text="Lenguaje de programación en C es creado por:\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Dennis Ritchie", width=15, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Linus Torvalds", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text=" Bill Gates", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_7_CAT2(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=900)

    P = Text(window, text="¿Quién dirigió el equipo para construir el código en el Proyecto Apollo?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text=" Grace Hopper", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="J.K Rowling", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Margaret Hamilton", width=15, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_8_CAT2(puntos):
    puntos_negativos = -1 * puntos
    window = Window(app, layout="auto", bg="#050A5A", height=400, width=650)

    P = Text(window, text="Deep Blue ganó su partida de ajedrez en el año...\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="1996", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="1988", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="2000", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_9_CAT2(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=550)

    P = Text(window, text="Primera “calculadora” creada en 4000 a.c\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Abaco", width=16, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Calculadora mecánica", width=16, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Casio", width=16, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_10_CAT2(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="Primer lenguaje de programación\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="C", width=13, height=2, command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Linux", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Fortran", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTAS_RANDOM_CAT2(case):
    preguntas_random_cat2

    if case == 100:
        return preguntas_random_cat2[0](case)
    elif case == 200:
        return preguntas_random_cat2[1](case)
    elif case == 300:
        return preguntas_random_cat2[2](case)
    elif case == 400:
        return preguntas_random_cat2[3](case)
    else:
        return preguntas_random_cat2[4](case)


# ------------------------FUNCIONES DE CATEGORIA 3------------------------#

def CATEGORIA_3(x):
    CAT_3 = Box(GAME_BOARD, layout="auto", grid=[x, 0])

    Titulo = Text(CAT_3, text="    Cultura General    ", color="yellow")

    B100 = PushButton(CAT_3, text="100", command=lambda: [PREGUNTAS_RANDOM_CAT3(100), DISABLE(B100)], width=6, height=1)
    B100.text_color = "white"
    B100.text_size = 17

    B200 = PushButton(CAT_3, text="200", command=lambda: [PREGUNTAS_RANDOM_CAT3(200), DISABLE(B200)], width=6, height=1)
    B200.text_color = "white"
    B200.text_size = 17

    B300 = PushButton(CAT_3, text="300", command=lambda: [PREGUNTAS_RANDOM_CAT3(300), DISABLE(B300)], width=6, height=1)
    B300.text_color = "white"
    B300.text_size = 17

    B400 = PushButton(CAT_3, text="400", command=lambda: [PREGUNTAS_RANDOM_CAT3(400), DISABLE(B400)], width=6, height=1)
    B400.text_color = "white"
    B400.text_size = 17

    B500 = PushButton(CAT_3, text="500", command=lambda: [PREGUNTAS_RANDOM_CAT3(500), DISABLE(B500)], width=6, height=1)
    B500.text_color = "white"
    B500.text_size = 17


def PREGUNTA_1_CAT3(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Qué libro escribió Mary Shelley?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="El Principito", width=19, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Frankenstein", width=19, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Los Juegos del Hambre", width=19, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_2_CAT3(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=550, height=400)

    P = Text(window, text="¿Cuál es el río más largo del mundo?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Nilo", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Bravo", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Amazonas", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_3_CAT3(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=600)

    P = Text(window, text="¿Cuántos huesos hay en el cuerpo humano?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="206", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="216", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="205", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_4_CAT3(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Cuántos años duró la Gran Guerra?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="4 años", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="5 años", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="2 años", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_5_CAT3(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Quién pintó la última cena?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Picasso", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Leonardo Da Vinci", width=14, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Tamayo", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_6_CAT3(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Qué es el opio?\n", )
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Banda musical", width=27, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 14
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Tipo de zapato", width=27, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 14
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Planta que contiene una droga narcótica", width=27, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 14
    C.font = "verdana 15 bold"


def PREGUNTA_7_CAT3(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=650, height=400)

    P = Text(window, text="Nombre de la bomba de Hiroshima y Nagasaki\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Little Boy y Fat Man", width=15, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="B83 y Castle Bravo", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="RDS-1 y Trinity", width=15, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_8_CAT3(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=550, height=400)

    P = Text(window, text="¿Cuál es el órgano más grande del cuerpo?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Corazón", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="La piel", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Páncreas", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_9_CAT3(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Cuando cayó el muro de Berlín?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="1945", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="1966", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="1989", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_10_CAT3(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="Homero escribió…\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Don Quijote de la Mancha", width=26, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="La Ilíada y La Odisea", width=26, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="La divina comedia", width=26, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTAS_RANDOM_CAT3(case):
    preguntas_random_cat3

    if case == 100:
        return preguntas_random_cat3[0](case)
    elif case == 200:
        return preguntas_random_cat3[1](case)
    elif case == 300:
        return preguntas_random_cat3[2](case)
    elif case == 400:
        return preguntas_random_cat3[3](case)
    else:
        return preguntas_random_cat3[4](case)


# ------------------------FUNCIONES DE CATEGORIA 4------------------------#

def CATEGORIA_4(x):
    CAT_4 = Box(GAME_BOARD, layout="auto", grid=[x, 0])

    Titulo = Text(CAT_4, text="       Big Data        ", color="yellow")
    B100 = PushButton(CAT_4, text="100", command=lambda: [PREGUNTAS_RANDOM_CAT4(100), DISABLE(B100)], width=6, height=1)
    B100.text_color = "white"
    B100.text_size = 17

    B200 = PushButton(CAT_4, text="200", command=lambda: [PREGUNTAS_RANDOM_CAT4(200), DISABLE(B200)], width=6, height=1)
    B200.text_color = "white"
    B200.text_size = 17

    B300 = PushButton(CAT_4, text="300", command=lambda: [PREGUNTAS_RANDOM_CAT4(300), DISABLE(B300)], width=6, height=1)
    B300.text_color = "white"
    B300.text_size = 17

    B400 = PushButton(CAT_4, text="400", command=lambda: [PREGUNTAS_RANDOM_CAT4(400), DISABLE(B400)], width=6, height=1)
    B400.text_color = "white"
    B400.text_size = 17

    B500 = PushButton(CAT_4, text="500", command=lambda: [PREGUNTAS_RANDOM_CAT4(500), DISABLE(B500)], width=6, height=1)
    B500.text_color = "white"
    B500.text_size = 17


def PREGUNTA_1_CAT4(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=350, width=670)

    P = Text(window, text="Big data es un término que describe")
    P.text_size = 20
    P.text_color = "yellow"

    P = Text(window, text="el gran volumen de datos con una velocidad superior?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Verdadero", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Falso", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTA_2_CAT4(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="Las tres ‘V’ de Big Data son:\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Veracidad, velocidad y volatilidad", width=27, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 13
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Volumen, velocidad y veracidad ", width=27, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 13
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Volumen, velocidad y variedad", width=27, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 13
    C.font = "verdana 15 bold"


def PREGUNTA_3_CAT4(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=670)

    P = Text(window, text="Modelo de programación más utilizado para Big Data\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Hash", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Biometrics", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Mapreduce", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_4_CAT4(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=350, width=550)

    P = Text(window, text="Algunos beneficios del Big Data son:")
    P.text_size = 20
    P.text_color = "yellow"

    P = Text(window, text="mayor eficiencia y menor atencion al cliente\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Verdadero", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Falso", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTA_5_CAT4(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=700, height=350)

    P = Text(window, text="Volumen se refiere a que haya más de un tipo de datos de texto,")
    P.text_size = 17
    P.text_color = "yellow"

    P = Text(window, text="imágenes o audios?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Verdadero", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Falso", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTA_6_CAT4(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=700, height=450)

    P = Text(window, text="Big Data ayuda a mejorar la ______ al recopilar")
    P.text_size = 20
    P.text_color = "yellow"

    P = Text(window, text="datos de redes sociales e internet\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Experiencia con el cliente", width=19, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Fabricación de materiales", width=19, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Creación de fraudes", width=19, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_7_CAT4(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="Tipos de Big Data según su estructura:\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Datos estructurados y estructura abierta", width=42, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 12
    A.font = "verdana 11 bold"

    B = PushButton(window, text="Datos estructurados, no estructurados y semiestructurados", width=42, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 11
    B.font = "verdana 11 bold"

    C = PushButton(window, text="Datos no estructurados y semiestructurados", width=42, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 12
    C.font = "verdana 11 bold"


def PREGUNTA_8_CAT4(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=700, height=350)

    P = Text(window, text="¿La Big Data puede implementarse para reconocer caras")
    P.text_color = "yellow"
    P.text_size = 20

    P = Text(window, text=" de gente que han estado en un lugar?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Verdadero", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Falso", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTA_9_CAT4(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=600)

    P = Text(window, text="Los tres pasos cómo funciona la Big Data son:\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Integrar, administrar y analizar la información", width=40, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 13
    A.font = "verdana 13 bold"

    B = PushButton(window, text="Dato, Hash, Dato anterior", width=40, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 13
    B.font = "verdana 13 bold"

    C = PushButton(window, text="Integrar, administrar y almacenar datos", width=40, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 13
    C.font = "verdana 13 bold"


def PREGUNTA_10_CAT4(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=700)

    P = Text(window, text="¿A quien se le da el crédito por usar el término Big Data?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="John Mashey", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="John Wick", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="John Cena", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTAS_RANDOM_CAT4(case):
    preguntas_random_cat4

    if case == 100:
        return preguntas_random_cat4[0](case)
    elif case == 200:
        return preguntas_random_cat4[1](case)
    elif case == 300:
        return preguntas_random_cat4[2](case)
    elif case == 400:
        return preguntas_random_cat4[3](case)
    else:
        return preguntas_random_cat4[4](case)


# ------------------------FUNCIONES DE CATEGORIA 5------------------------#

def CATEGORIA_5(x):
    CAT_5 = Box(GAME_BOARD, layout="auto", grid=[x, 0])

    Titulo = Text(CAT_5, text="          IoT          ", color="yellow")

    B100 = PushButton(CAT_5, text="100", command=lambda: [PREGUNTAS_RANDOM_CAT5(100), DISABLE(B100)], width=6, height=1)
    B100.text_color = "white"
    B100.text_size = 17

    B200 = PushButton(CAT_5, text="200", command=lambda: [PREGUNTAS_RANDOM_CAT5(200), DISABLE(B200)], width=6, height=1)
    B200.text_color = "white"
    B200.text_size = 17

    B300 = PushButton(CAT_5, text="300", command=lambda: [PREGUNTAS_RANDOM_CAT5(300), DISABLE(B300)], width=6, height=1)
    B300.text_color = "white"
    B300.text_size = 17

    B400 = PushButton(CAT_5, text="400", command=lambda: [PREGUNTAS_RANDOM_CAT5(400), DISABLE(B400)], width=6, height=1)
    B400.text_color = "white"
    B400.text_size = 17

    B500 = PushButton(CAT_5, text="500", command=lambda: [PREGUNTAS_RANDOM_CAT5(500), DISABLE(B500)], width=6, height=1)
    B500.text_color = "white"
    B500.text_size = 17


def PREGUNTA_1_CAT5(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="La principal área donde se utilizan IOTs\n")
    P.text_color = "yellow"
    P.text_size = 19

    A = PushButton(window, text="En el hogar", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Área industrial ", width=14, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Área médica", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_2_CAT5(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="Ejemplo de IOT\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Televisión", width=17, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Apple pencil", width=17, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Refrigerador ", width=17, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_3_CAT5(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=350, width=750)

    P = Text(window, text="Es imposible hackear un IOT,")
    P.text_color = "yellow"
    P.text_size = 20

    P = Text(window, text="pues no tiene interacción humana\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Verdadero", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Falso", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTA_4_CAT5(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=650, height=350)

    P = Text(window, text="Las compañías que producen aparatos IoT pueden obtener ")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="y vender la información personal de sus usuarios.\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Verdadero", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Falso", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTA_5_CAT5(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=720, height=400)

    P = Text(window, text="¿Cuándo se empezó a usar el término IOT por Kevin Ashton?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="1987", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="2000", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="1999", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_6_CAT5(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=350, width=700)

    P = Text(window, text="¿La mayoría de las máquinas con IOT")
    P.text_size = 20
    P.text_color = "yellow"

    P = Text(window, text="son amigables con el ambiente?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Verdadero", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Falso", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTA_7_CAT5(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=650)

    P = Text(window, text="¿Cuál es considerada la primera máquina con IOT?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Maquina expendedora de Coca-Cola", width=28, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 13
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Refrigerador", width=28, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 13
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Automóvil", width=28, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 13
    C.font = "verdana 15 bold"


def PREGUNTA_8_CAT5(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=600)

    P = Text(window, text="¿Qué tipo de aparato no es considerado IOT?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Amazon Go checkout store", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Gadgets", width=20, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Nest thermostat", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_9_CAT5(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=600)

    P = Text(window, text="¿Cosas necesarias para que funcione un IOT?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Software,Hardware, Conectividad y volumen", width=34, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 13
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Hardware, Datos y conectividad", width=34, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 13
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Hardware, Software, Datos y Conectividad", width=34, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 13
    C.font = "verdana 15 bold"


def PREGUNTA_10_CAT5(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=350, width=650)

    P = Text(window, text="Un aparato IOT puede recibir y enviar información")
    P.text_size = 20
    P.text_color = "yellow"

    P = Text(window, text="sin necesidad de ejecutar alguna acción\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Verdadero", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Falso", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTAS_RANDOM_CAT5(case):
    preguntas_random_cat5

    if case == 100:
        return preguntas_random_cat5[0](case)
    elif case == 200:
        return preguntas_random_cat5[1](case)
    elif case == 300:
        return preguntas_random_cat5[2](case)
    elif case == 400:
        return preguntas_random_cat5[3](case)
    else:
        return preguntas_random_cat5[4](case)


# ------------------------FUNCIONES DE CATEGORIA 6------------------------#

def CATEGORIA_6(x):
    CAT_6 = Box(GAME_BOARD, layout="auto", grid=[x, 0])

    Titulo = Text(CAT_6, text="        México         ", color="yellow")

    B100 = PushButton(CAT_6, text="100", command=lambda: [PREGUNTAS_RANDOM_CAT6(100), DISABLE(B100)], width=6, height=1)
    B100.text_color = "white"
    B100.text_size = 17

    B200 = PushButton(CAT_6, text="200", command=lambda: [PREGUNTAS_RANDOM_CAT6(200), DISABLE(B200)], width=6, height=1)
    B200.text_color = "white"
    B200.text_size = 17

    B300 = PushButton(CAT_6, text="300", command=lambda: [PREGUNTAS_RANDOM_CAT6(300), DISABLE(B300)], width=6, height=1)
    B300.text_color = "white"
    B300.text_size = 17

    B400 = PushButton(CAT_6, text="400", command=lambda: [PREGUNTAS_RANDOM_CAT6(400), DISABLE(B400)], width=6, height=1)
    B400.text_color = "white"
    B400.text_size = 17

    B500 = PushButton(CAT_6, text="500", command=lambda: [PREGUNTAS_RANDOM_CAT6(500), DISABLE(B500)], width=6, height=1)
    B500.text_color = "white"
    B500.text_size = 17


def PREGUNTA_1_CAT6(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=600)

    P = Text(window, text="¿Qué mexicano inventó la televisión a color?\n")
    P.text_color = "yellow"
    P.text_size = 18

    A = PushButton(window, text="Guilermo González Camarena", width=25, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 13
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Mario Molina", width=25, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 13
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Miramontes", width=25, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 13
    C.font = "verdana 15 bold"


def PREGUNTA_2_CAT6(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=450, width=700)

    P = Text(window, text="Es la pirámide más grande del mundo en volúmen, no en altura,")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="y se encuentra en México, ¿Cuál es su nombre?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="El templo de Kukulkán", width=25, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Pirámides del Tajín", width=25, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="La Gran Pirámide de Cholula", width=25, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_3_CAT6(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=600)

    P = Text(window, text="¿Qué famoso líder militar de la Revolución mexicana")
    P.text_color = "yellow"
    P.text_size = 15

    P = Text(window, text="fue conocido como <<Caudillo del Sur>>?\n")
    P.text_color = "yellow"
    P.text_size = 15

    A = PushButton(window, text="Francisco I. Madero", width=25, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Emiliano Zapata", width=25, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Pancho Villa", width=25, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_4_CAT6(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Qué sucedió de 1810-1821?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="La Independencia de México", width=22, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Revolución Mexicana", width=22, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Miramontes", width=22, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_5_CAT6(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=650)

    P = Text(window, text="¿Qué escribió Francisco González Bocanegra?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="El Himno Nacional", width=19, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="La canción El Noa Noa", width=19, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="El juramento a la Bandera", width=19, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_6_CAT6(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Cuál era el trabajo de la Malinche?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Esposa de un monarca", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Guerrera", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Traductora/Intérprete", width=20, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_7_CAT6(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=450)

    P = Text(window, text="¿Cómo se llama el diplomático")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="conocido como el <<Schindler mexicano>>?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Gilberto del Bosque", width=20, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Miguel Hidalgo", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Octavio Paz", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_8_CAT6(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=450, width=650)

    P = Text(window, text="¿Cómo se llama la salsa típica mexicana")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="que está compuesta por más de 20 ingredientes?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Salsa Chipotle", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Mole", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Salsa Borracha", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_9_CAT6(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=700)

    P = Text(window, text="¿Cuál es el teatro más importante de México?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Teatro Metropolitano", width=19, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Teatro Degollado", width=19, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="El palacio de Bellas Artes", width=19, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_10_CAT6(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=450, width=700)

    P = Text(window, text="¿Qué famoso cantante mexicano")
    P.text_color = "yellow"
    P.text_size = 20

    P = Text(window, text="interpreta la canción de <<Las Golondrínas>>?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Jorge Negrete", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Pedro Infante", width=13, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Javier Solis", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTAS_RANDOM_CAT6(case):
    preguntas_random_cat6

    if case == 100:
        return preguntas_random_cat6[0](case)
    elif case == 200:
        return preguntas_random_cat6[1](case)
    elif case == 300:
        return preguntas_random_cat6[2](case)
    elif case == 400:
        return preguntas_random_cat6[3](case)
    else:
        return preguntas_random_cat6[4](case)


# ------------------------FUNCIONES DE CATEGORIA 7------------------------#

def CATEGORIA_7(x):
    CAT_7 = Box(GAME_BOARD, layout="auto", grid=[x, 0])

    Titulo = Text(CAT_7, text="  Películas y Series   ", color="yellow")

    B100 = PushButton(CAT_7, text="100", command=lambda: [PREGUNTAS_RANDOM_CAT7(100), DISABLE(B100)], width=6, height=1)
    B100.text_color = "white"
    B100.text_size = 17

    B200 = PushButton(CAT_7, text="200", command=lambda: [PREGUNTAS_RANDOM_CAT7(200), DISABLE(B200)], width=6, height=1)
    B200.text_color = "white"
    B200.text_size = 17

    B300 = PushButton(CAT_7, text="300", command=lambda: [PREGUNTAS_RANDOM_CAT7(300), DISABLE(B300)], width=6, height=1)
    B300.text_color = "white"
    B300.text_size = 17

    B400 = PushButton(CAT_7, text="400", command=lambda: [PREGUNTAS_RANDOM_CAT7(400), DISABLE(B400)], width=6, height=1)
    B400.text_color = "white"
    B400.text_size = 17

    B500 = PushButton(CAT_7, text="500", command=lambda: [PREGUNTAS_RANDOM_CAT7(500), DISABLE(B500)], width=6, height=1)
    B500.text_color = "white"
    B500.text_size = 17


def PREGUNTA_1_CAT7(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400)

    P = Text(window, text="¿Cuál es la serie más vista?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Lost", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="The Walking Dead", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Game of Thrones", width=14, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_2_CAT7(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=450)

    P = Text(window, text="En la pélicula Mátrix,")
    P.text_color = "yellow"
    P.text_size = 20

    P = Text(window, text="¿Neo toma la pastillla de qué color?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Roja", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Azul", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Verde", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_3_CAT7(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=650)

    P = Text(window, text="¿Qué actor de Hollywood actúa con su mismo papel en Zombieland?")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Woody Harrelson", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Jesse Eisenberg", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Bill Murray", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_4_CAT7(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=450, width=650)

    P = Text(window, text="En Risky Business,")
    P.text_color = "yellow"
    P.text_size = 20

    P = Text(window, text="¿Qué canción canta Tom Cruise en ropa interior?\n")
    P.text_color = "yellow"
    P.text_size = 22

    A = PushButton(window, text="Johnny B. Goode", width=22, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Old Time Rock n Roll", width=22, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="I Dont Want to Miss a Thing", width=22, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_5_CAT7(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=600)

    P = Text(window, text="¿En qué ciudad de EUA toma lugar la serie Gossip Girl?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Los Angeles", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Chicago", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Nueva York", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_6_CAT7(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=450, width=650)

    P = Text(window, text="Serie de comedia de amigos científicos")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="donde su primer amiga es su vecina llamada Penny\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Silicon Valley", width=16, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="The Big Bang Theory", width=16, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="The Office", width=16, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_7_CAT7(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=680)

    P = Text(window, text="¿Qué serie se encuentra en el mismo universo que Breaking Bad?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Friends", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Supernatural", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="The Walking Dead", width=14, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_8_CAT7(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=700)

    P = Text(window, text="¿En qué año se estrenó la primera película de la Saga de Star Wars?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="1977", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="1979", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="1972", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_9_CAT7(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=700)

    P = Text(window, text="¿Qué estrella del cine muere en la cena inicial de la pelícua Scream?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Jennifer López", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Drew Barrymore", width=13, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Alicia Silverstone", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_10_CAT7(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=600, height=300)

    P = Text(window, text="En la película The Notebook, los actores protagonistas")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="tenían una buena relación durante el rodaje de la película\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Falso", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Verdadero", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTAS_RANDOM_CAT7(case):
    preguntas_random_cat7

    if case == 100:
        return preguntas_random_cat7[0](case)
    elif case == 200:
        return preguntas_random_cat7[1](case)
    elif case == 300:
        return preguntas_random_cat7[2](case)
    elif case == 400:
        return preguntas_random_cat7[3](case)
    else:
        return preguntas_random_cat7[4](case)


# ------------------------FUNCIONES DE CATEGORIA 8------------------------#

def CATEGORIA_8(x):
    CAT_8 = Box(GAME_BOARD, layout="auto", grid=[x, 0])

    Titulo = Text(CAT_8, text="        Comida         ", color="yellow")
    B100 = PushButton(CAT_8, text="100", command=lambda: [PREGUNTAS_RANDOM_CAT8(100), DISABLE(B100)], width=6, height=1)
    B100.text_color = "white"
    B100.text_size = 17

    B200 = PushButton(CAT_8, text="200", command=lambda: [PREGUNTAS_RANDOM_CAT8(200), DISABLE(B200)], width=6, height=1)
    B200.text_color = "white"
    B200.text_size = 17

    B300 = PushButton(CAT_8, text="300", command=lambda: [PREGUNTAS_RANDOM_CAT8(300), DISABLE(B300)], width=6, height=1)
    B300.text_color = "white"
    B300.text_size = 17

    B400 = PushButton(CAT_8, text="400", command=lambda: [PREGUNTAS_RANDOM_CAT8(400), DISABLE(B400)], width=6, height=1)
    B400.text_color = "white"
    B400.text_size = 17

    B500 = PushButton(CAT_8, text="500", command=lambda: [PREGUNTAS_RANDOM_CAT8(500), DISABLE(B500)], width=6, height=1)
    B500.text_color = "white"
    B500.text_size = 17


def PREGUNTA_1_CAT8(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=650)

    P = Text(window, text="¿De qué país es la Paella?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="España", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Argentína", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Brasil", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_2_CAT8(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=650, height=400)

    P = Text(window, text="¿Qué es el Zacahuil y de qué país es?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Es un tipo de arroz de Japón", width=33, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 13
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Es un tamal mexicano que pesa 70kg.", width=33, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 13
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Es un insecto usado en platillos mexicanos", width=33, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 13
    C.font = "verdana 15 bold"


def PREGUNTA_3_CAT8(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=700)

    P = Text(window, text="¿Qué país es tan fanático del Curry como la India?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Africa", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Bolivia", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Reino Unido", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_4_CAT8(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=700, height=400)

    P = Text(window, text="¿Qué alimento era considerado como medicina contra la diarrea?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Pan", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Ketchup", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Pasas", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_5_CAT8(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=600, height=450)

    P = Text(window, text="¿Qué cultura Mesoamericana utilizaba")
    P.text_color = "yellow"
    P.text_size = 20

    P = Text(window, text="la cocoa como sistema monetario ?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Los Mexicas", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Los Olmecas", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Los Mayas", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_6_CAT8(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=700)

    P = Text(window, text="¿De dónde son originarias las papas frítas/a la francesa?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Bélgica", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Francia", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Estados Unidos", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_7_CAT8(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=700)

    P = Text(window, text="¿Nuestro ADN es 60% similar al de qué fruta?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Ciruela Pasa", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Plátano", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Fresa", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_8_CAT8(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=600)

    P = Text(window, text="¿Qué alimento contiene mas calorías?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Hamburguesa", width=16, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Hot-Dog", width=16, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="La Ensalada Cesar", width=16, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_9_CAT8(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=600, height=400)

    P = Text(window, text="El chile más picoso del mundo es:\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Carolina Reaper", width=13, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Chile Habanero", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Chile Chiltepin", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_10_CAT8(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=650)

    P = Text(window, text="El platillo favorito de los mexicanos es...\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Tortas", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Tacos", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Enchiladas", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTAS_RANDOM_CAT8(case):
    preguntas_random_cat8

    if case == 100:
        return preguntas_random_cat8[0](case)
    elif case == 200:
        return preguntas_random_cat8[1](case)
    elif case == 300:
        return preguntas_random_cat8[2](case)
    elif case == 400:
        return preguntas_random_cat8[3](case)
    else:
        return preguntas_random_cat8[4](case)


# ------------------------FUNCIONES DE CATEGORIA 9------------------------#

def CATEGORIA_9(x):
    CAT_9 = Box(GAME_BOARD, layout="auto", grid=[x, 0])

    Titulo = Text(CAT_9, text="     Hacking Tools     ", color="yellow")

    B100 = PushButton(CAT_9, text="100", command=lambda: [PREGUNTAS_RANDOM_CAT9(100), DISABLE(B100)], width=6, height=1)
    B100.text_color = "white"
    B100.text_size = 17

    B200 = PushButton(CAT_9, text="200", command=lambda: [PREGUNTAS_RANDOM_CAT9(200), DISABLE(B200)], width=6, height=1)
    B200.text_color = "white"
    B200.text_size = 17

    B300 = PushButton(CAT_9, text="300", command=lambda: [PREGUNTAS_RANDOM_CAT9(300), DISABLE(B300)], width=6, height=1)
    B300.text_color = "white"
    B300.text_size = 17

    B400 = PushButton(CAT_9, text="400", command=lambda: [PREGUNTAS_RANDOM_CAT9(400), DISABLE(B400)], width=6, height=1)
    B400.text_color = "white"
    B400.text_size = 17

    B500 = PushButton(CAT_9, text="500", command=lambda: [PREGUNTAS_RANDOM_CAT9(500), DISABLE(B500)], width=6, height=1)
    B500.text_color = "white"
    B500.text_size = 17


def PREGUNTA_1_CAT9(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=300, width=650)

    P = Text(window, text="Las Hacking Tools ayudan a evitar")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="que alguien malicioso vea mis datos e informacion\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Falso", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Verdadero", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTA_2_CAT9(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=650)

    P = Text(window, text="¿Como se les llama a los hackers que utilizan")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="sus conocimientos para generar mayor seguridad\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Hackers de sombrero blanco", width=22, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 13
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Hackers de sombrero gris", width=22, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 13
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Hackers de sombrero negro", width=22, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 13
    C.font = "verdana 15 bold"


def PREGUNTA_3_CAT9(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=700)

    P = Text(window, text="¿Cuáles son unas de las herramientas más utilizadas para hackear?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="McAfee y Avast", width=26, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 13
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Kali Linux y Avira", width=26, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 13
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Kali Linux y Parrot Security OS", width=26, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 13
    C.font = "verdana 15 bold"


def PREGUNTA_4_CAT9(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=740, height=400)

    P = Text(window, text="Programa de criptografía que aplica fuerza bruta para decifrar contraseñas\n")
    P.text_color = "yellow"
    P.text_size = 16

    A = PushButton(window, text="Phishing", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="John The Ripper", width=20, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Fiddler", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_5_CAT9(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=700)

    P = Text(window, text="La inyección SQL es un _______ a un sitio web\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Hacking Tool", width=18, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Anti-Hacking Tool", width=18, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Antivirus", width=18, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_6_CAT9(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=300, width=700)

    P = Text(window, text="¿En México puedes ir a la carcel por cometer algún delíto online\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Verdadero", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Falso", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTA_7_CAT9(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=720)

    P = Text(window, text="¿De cuanto tiempo es la pena contra quien realiza hackeo en México?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="De 4 a 12 meses", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 13
    A.font = "verdana 15 bold"

    B = PushButton(window, text="De 6 meses a 2 años", width=20, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 13
    B.font = "verdana 15 bold"

    C = PushButton(window, text="De 6 meses a 4 años", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 13
    C.font = "verdana 15 bold"


def PREGUNTA_8_CAT9(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=450, width=700)

    P = Text(window, text="¿En qué año Cambridge Analítica usó perfiles de Facebook")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="para crear propaganda de un partído político estadunidense?\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="2020", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="2018", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="2014", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_9_CAT9(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=650)

    P = Text(window, text="¿Anonymous es considerado un hacker?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Verdadero", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Falso", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTA_10_CAT9(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=300, width=700)

    P = Text(window, text="¿Aircrack Ng permite realizar ataques de fuerza bruta")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="sobre redes Wifi para obtener contraseñas de las mismas?")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Verdadero", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Falso", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"


def PREGUNTAS_RANDOM_CAT9(case):
    preguntas_random_cat9

    if case == 100:
        preguntas_random_cat9[0](case)
    elif case == 200:
        preguntas_random_cat9[1](case)
    elif case == 300:
        preguntas_random_cat9[2](case)
    elif case == 400:
        preguntas_random_cat9[3](case)
    else:
        preguntas_random_cat9[4](case)


# ------------------------FUNCIONES DE CATEGORIA 10------------------------#

def CATEGORIA_10(x):
    CAT_10 = Box(GAME_BOARD, layout="auto", grid=[x, 0])

    Titulo = Text(CAT_10, text="Quizzes del Profe Jerry", color="yellow")
    B100 = PushButton(CAT_10, text="100", command=lambda: [PREGUNTAS_RANDOM_CAT10(100), DISABLE(B100)], width=6,
                      height=1)
    B100.text_color = "white"
    B100.text_size = 17

    B200 = PushButton(CAT_10, text="200", command=lambda: [PREGUNTAS_RANDOM_CAT10(200), DISABLE(B200)], width=6,
                      height=1)
    B200.text_color = "white"
    B200.text_size = 17

    B300 = PushButton(CAT_10, text="300", command=lambda: [PREGUNTAS_RANDOM_CAT10(300), DISABLE(B300)], width=6,
                      height=1)
    B300.text_color = "white"
    B300.text_size = 17

    B400 = PushButton(CAT_10, text="400", command=lambda: [PREGUNTAS_RANDOM_CAT10(400), DISABLE(B400)], width=6,
                      height=1)
    B400.text_color = "white"
    B400.text_size = 17

    B500 = PushButton(CAT_10, text="500", command=lambda: [PREGUNTAS_RANDOM_CAT10(500), DISABLE(B500)], width=6,
                      height=1)
    B500.text_color = "white"
    B500.text_size = 17


def PREGUNTA_1_CAT10(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=650, height=400)

    P = Text(window, text="Qué significa CETYS\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Centro de Estudios Técnicos y Superiores", width=34, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 13
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Centro de Enseñanza Técnica y Superior", width=34, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 13
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Centro de Enseñanza Tecnisista", width=34, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 13
    C.font = "verdana 15 bold"


def PREGUNTA_2_CAT10(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=450, width=700)

    P = Text(window, text="_____ Es la aplicación del conocimiento que da")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="la ciencia para construir tecnología y resolver alguna problemática\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Tecnología", width=17, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Conocimiento", width=17, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Ingeniería", width=17, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_3_CAT10(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=650)

    P = Text(window, text="¿Cuál es el primer logro de la ingeniería?\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Acueductos", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="La agriultura", width=14, height=2,
                   command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="La rueda", width=14, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_4_CAT10(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=650, height=400)

    P = Text(window, text="¿Cuál es el siglo con mayor inventos tecnológicos\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Siglo XXI", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Siglo XIX", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Siglo XX", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_5_CAT10(puntos):
    puntos_negativos = -1 * puntos
    window = Window(app, layout="auto", bg="#050A5A", width=650, height=400)

    P = Text(window, text="Tipo de tecnología que no es tangible\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Blanda", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Dura", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Aguada", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_6_CAT10(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=720, height=400)

    P = Text(window, text="Una idea que ya cuenta con una comprobacion es llamada...\n")
    P.text_color = "yellow"
    P.text_size = 18

    A = PushButton(window, text="Innovación", width=18, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Hipótessis", width=18, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Teoría", width=18, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_7_CAT10(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=400, width=700)

    P = Text(window, text="Nombre del examen que se realiza para obtener el titulo de una carrera\n")
    P.text_color = "yellow"
    P.text_size = 16

    A = PushButton(window, text="College Board", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Ceneval", width=20, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Enlace", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_8_CAT10(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=700, height=400)

    P = Text(window, text="Es la unidad básica de la computación para guardar información\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Bit", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Byte", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Vit", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_9_CAT10(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", width=650, height=450)

    P = Text(window, text="Nombre de la primera persona llamada Ingeniero\n")
    P.text_color = "yellow"
    P.text_size = 20

    A = PushButton(window, text="Imhotep", width=20, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="James Watt", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Arthur Casagrande", width=20, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTA_10_CAT10(puntos):
    puntos_negativos = -1 * puntos

    window = Window(app, layout="auto", bg="#050A5A", height=450, width=740)

    P = Text(window, text="Técnicas que persiguen el engaño a una víctima ganándose su")
    P.text_color = "yellow"
    P.text_size = 17

    P = Text(window, text="confianza haciéndose pasar por una persona para robar su información\n")
    P.text_color = "yellow"
    P.text_size = 17

    A = PushButton(window, text="Spoofing", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    A.bg = "navy"
    A.text_color = "white"
    A.text_size = 15
    A.font = "verdana 15 bold"

    B = PushButton(window, text="Phishing", width=13, height=2, command=lambda: [CONTADOR(puntos, ), CLOSE(window)])
    B.bg = "navy"
    B.text_color = "white"
    B.text_size = 15
    B.font = "verdana 15 bold"

    C = PushButton(window, text="Vishing", width=13, height=2,
                   command=lambda: [CONTADOR(puntos_negativos, ), CLOSE(window)])
    C.bg = "navy"
    C.text_color = "white"
    C.text_size = 15
    C.font = "verdana 15 bold"


def PREGUNTAS_RANDOM_CAT10(case):
    if case == 100:
        return preguntas_random_cat10[0](case)
    elif case == 200:
        return preguntas_random_cat10[1](case)
    elif case == 300:
        return preguntas_random_cat10[2](case)
    elif case == 400:
        return preguntas_random_cat10[3](case)
    else:
        return preguntas_random_cat10[4](case)


# VARIABLES ---------------

preguntas_cat1 = [PREGUNTA_1_CAT1, PREGUNTA_2_CAT1, PREGUNTA_3_CAT1, PREGUNTA_4_CAT1, PREGUNTA_5_CAT1, PREGUNTA_6_CAT1,
                  PREGUNTA_7_CAT1, PREGUNTA_8_CAT1, PREGUNTA_9_CAT1, PREGUNTA_10_CAT1]
preguntas_random_cat1 = random.sample(preguntas_cat1, 5)

preguntas_cat2 = [PREGUNTA_1_CAT2, PREGUNTA_2_CAT2, PREGUNTA_3_CAT2, PREGUNTA_4_CAT2, PREGUNTA_5_CAT2, PREGUNTA_6_CAT2,
                  PREGUNTA_7_CAT2, PREGUNTA_8_CAT2, PREGUNTA_9_CAT2, PREGUNTA_10_CAT2]
preguntas_random_cat2 = random.sample(preguntas_cat2, 5)

preguntas_cat3 = [PREGUNTA_1_CAT3, PREGUNTA_2_CAT3, PREGUNTA_3_CAT3, PREGUNTA_4_CAT3, PREGUNTA_5_CAT3, PREGUNTA_6_CAT3,
                  PREGUNTA_7_CAT3, PREGUNTA_8_CAT3, PREGUNTA_9_CAT3, PREGUNTA_10_CAT3]
preguntas_random_cat3 = random.sample(preguntas_cat3, 5)

preguntas_cat4 = [PREGUNTA_1_CAT4, PREGUNTA_2_CAT4, PREGUNTA_3_CAT4, PREGUNTA_4_CAT4, PREGUNTA_5_CAT4, PREGUNTA_6_CAT4,
                  PREGUNTA_7_CAT4, PREGUNTA_8_CAT4, PREGUNTA_9_CAT4, PREGUNTA_10_CAT4]
preguntas_random_cat4 = random.sample(preguntas_cat4, 5)

preguntas_cat5 = [PREGUNTA_1_CAT5, PREGUNTA_2_CAT5, PREGUNTA_3_CAT5, PREGUNTA_4_CAT5, PREGUNTA_5_CAT5, PREGUNTA_6_CAT5,
                  PREGUNTA_7_CAT5, PREGUNTA_8_CAT5, PREGUNTA_9_CAT5, PREGUNTA_10_CAT5]
preguntas_random_cat5 = random.sample(preguntas_cat5, 5)

preguntas_cat6 = [PREGUNTA_1_CAT6, PREGUNTA_2_CAT6, PREGUNTA_3_CAT6, PREGUNTA_4_CAT6, PREGUNTA_5_CAT6, PREGUNTA_6_CAT6,
                  PREGUNTA_7_CAT6, PREGUNTA_8_CAT6, PREGUNTA_9_CAT6, PREGUNTA_10_CAT6]
preguntas_random_cat6 = random.sample(preguntas_cat6, 5)

preguntas_cat7 = [PREGUNTA_1_CAT7, PREGUNTA_2_CAT7, PREGUNTA_3_CAT7, PREGUNTA_4_CAT7, PREGUNTA_5_CAT7, PREGUNTA_6_CAT7,
                  PREGUNTA_7_CAT7, PREGUNTA_8_CAT7, PREGUNTA_9_CAT7, PREGUNTA_10_CAT7]
preguntas_random_cat7 = random.sample(preguntas_cat7, 5)

preguntas_cat8 = [PREGUNTA_1_CAT8, PREGUNTA_2_CAT8, PREGUNTA_3_CAT8, PREGUNTA_4_CAT8, PREGUNTA_5_CAT8, PREGUNTA_6_CAT8,
                  PREGUNTA_7_CAT8, PREGUNTA_8_CAT8, PREGUNTA_9_CAT8, PREGUNTA_10_CAT8]
preguntas_random_cat8 = random.sample(preguntas_cat8, 5)

preguntas_cat9 = [PREGUNTA_1_CAT9, PREGUNTA_2_CAT9, PREGUNTA_3_CAT9, PREGUNTA_4_CAT9, PREGUNTA_5_CAT9, PREGUNTA_6_CAT9,
                  PREGUNTA_7_CAT9, PREGUNTA_8_CAT9, PREGUNTA_9_CAT9, PREGUNTA_10_CAT9]
preguntas_random_cat9 = random.sample(preguntas_cat9, 5)

preguntas_cat10 = [PREGUNTA_1_CAT10, PREGUNTA_2_CAT10, PREGUNTA_3_CAT10, PREGUNTA_4_CAT10, PREGUNTA_5_CAT10,
                   PREGUNTA_6_CAT10, PREGUNTA_7_CAT10, PREGUNTA_8_CAT10, PREGUNTA_9_CAT10, PREGUNTA_10_CAT10]
preguntas_random_cat10 = random.sample(preguntas_cat10, 5)

board_size = 6

x = 0

contador = 0

botones_presionados = 0

# APP-------------------

app = App(title="Jeopardy", width=1000)

app.bg = "navy"

text_center = Text(app, text="Bienvenido al Jeopardy de Intro a ICS", color="yellow", size=30, font="Verdana bold")

GAME_BOARD = Box(app, layout="grid")

CATEGORIAS = [CATEGORIA_1, CATEGORIA_2, CATEGORIA_3, CATEGORIA_4, CATEGORIA_5, CATEGORIA_6, CATEGORIA_7, CATEGORIA_8,
              CATEGORIA_9, CATEGORIA_10]

CATEGORIAS_RANDOM = random.sample(CATEGORIAS, 6)  # escoge categorias random

for CAT in CATEGORIAS_RANDOM:
    CAT(x)
    x += 1

# ------------------------SCORE-----------------
CONT = Text(app, text="Puntos: " + str(contador), color="yellow", size=20)
app.display()
