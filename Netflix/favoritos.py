from peliculas import Peliculas
from series import Series
import random

#------------------------------PELICULAS---------------------------------------------------
pelicula_1 = Peliculas(titulo='The Notebook', duracion='2 h. 4 min', director= 'Director: Nick Cassavetes',
                       actores='Actores: Ryan Gosling y Rachel McAdams', clasificacion='PG-13', genero='Drama/romance',year=2004,
                       formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

pelicula_2 = Peliculas(titulo='Inception', duracion='2 h. 42 min', director='Director: Christopher Nolan',
                       actores='Actores: Leonardo DiCaprio y Ken Watanabe', clasificacion='PG-13',
                       genero='Drama/Suspenso/Accion',year=2010,
                       formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

pelicula_3 = Peliculas(titulo='Forrest Gump', duracion='2 h. 22 min', director='Director: Robert Zemeckis',
                       actores='Actores: Tom Hanks, Robin Wright, Gary Sinise', clasificacion='PG-13',
                       genero='Comedia/Drama',year=1994,
                       formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

pelicula_4 = Peliculas(titulo='Fight Club', duracion='2 h. 31 min', director='Director: Chris Gorak',
                       actores='Actores: Edward Norton, Brad Pitt', clasificacion='R', genero='Drama/Comedia negra',year=1999,
                       formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

pelicula_5 = Peliculas(titulo='Pulp Fiction', duracion='2 h. 58 min', director='Director: Quentin Tarantino',
                       actores='Actores: John Travolta, Samuel L. Jackson, Uma Thurman', clasificacion='R',
                       genero='Cine Policiaco',year=1994,
                       formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

pelicula_6 = Peliculas(titulo='Schindlers List ', duracion='3 h. 17 min ', director='Director: Steven Spielberg',
                       actores='Actores: Liam Neeson, Ralph Fiennes', clasificacion='PG-13',
                       genero='Cine bélico, cine biográfico y drama',year=1993,
                       formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

pelicula_7 = Peliculas(titulo='The Dark Knight', duracion='2 h. 32 min', director='Director: Christopher Nolan',
                       actores='Actores: Christian Bale, Michael Caine, Heath Ledger', clasificacion='PG-13',
                       genero='Accion/Drama',year=2008,
                       formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

pelicula_8 = Peliculas(titulo='The Godfather', duracion=' 2 h. 58 min', director='Director: Francis Ford Coppola',
                       actores='Actores: Marlon Brando, Al Pacino, Robert Duvall', clasificacion='R',
                       genero='Gánsteres/Drama',year=1972,
                       formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

pelicula_9 = Peliculas(titulo='Star Wars Episode IV - A New Hope', duracion='2 h. 5 min', director='Director: George Lucas',
                       actores='Actores: Mark Hamill, Harrison Ford, Carrie Fisher', clasificacion='PG',
                       genero='Ciencia Ficcion',year=1977,
                       formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

pelicula_10 = Peliculas(titulo='Hunger Games', duracion='2 h. 22 min', director='Director: Gary Ross',
                        actores='Actores: Jennifer Lawrence, Josh Hutcherson, Liam Hemsworth', clasificacion='PG-13',
                        genero='Ciencia FIccion, accion',year=2012,
                        formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

#------------------------------------SERIES---------------------------------------------------

serie_1 = Series(titulo='Friends', duracion="20 min", temporadas="10 temporadas", capitulos='236 capitulos',
                 actores='Actores: Jennifer Aniston, Courteney Cox,  Lisa Kudrow, Matt LeBlanc, Matthew Perry, David Schwimmer',
                 formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

serie_2 = Series(titulo='Breaking Bad', duracion="45 min", temporadas='5 temporadas', capitulos='62 capitulos',
                 actores='Actores: Bryan Cranston, Anna Gunn, Aaron Paul',
                 formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

serie_3 = Series(titulo='Game of Thrones', duracion="50 min", temporadas='8 temporadas', capitulos='73 capitulos',
                 actores='Actores: Emilia Clarke, Kit Harington, Sophie Turner',
                 formato=None, resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

serie_4 = Series(titulo='Greys Anatomy', duracion="45 min", temporadas='17 temporadas', capitulos='372 capitulos',
                 actores='Actores: Ellen Pompeo, Sandra Oh',
                 formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

serie_5 = Series(titulo='Dr. House', duracion="43 min", temporadas='8 temporadas', capitulos='177 capitulos',
                 actores='Actores: Hugh Laurie, Lisa Edelstein, Omar Epps',
                 formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

serie_6 = Series(titulo='The Office', duracion="22 min", temporadas='9 temporadas', capitulos='188 capitulos',
                 actores='Actores: Steve Carell, Jenna Fischer, John Krasinski, Rainn Wilson',
                 formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

serie_7 = Series(titulo='Lost', duracion="42 min", temporadas='6 temporadas', capitulos='121 capitulos',
                 actores='Actores: Matthew Fox, Adewale Akinnuoye-Agbaje, Sam Anderson',
                 formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

serie_8 = Series(titulo='The Big Bang Theory', duracion="30 min", temporadas='12 temporadas', capitulos='279 capitulos',
                 actores='Actores: Jim Parsons, Kaley Cuoco, Johnny Galecki, Kunal Nayyar, Simon Helberg',
                 formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

serie_9 = Series(titulo='Gossip Girl', duracion="45 min", temporadas='6 temporadas', capitulos='121 capitulos',
                actores='Actores: Blake Lively, Leighton Meester, Penn Badgley, Chace Crawford, Ed Westwick',
                formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

serie_10 = Series(titulo='The Mandalorian', duracion="31 min", temporadas='2 temporadas', capitulos='16 capitulos',
                  actores='Actores: Pedro Pascal',formato=None,resolucion=None, velocidad_de_reproduccion=None, subtitulos=None)

lista_peliculas_series = [pelicula_1, pelicula_2, pelicula_3, pelicula_4, pelicula_5,
                       pelicula_6, pelicula_7, pelicula_8, pelicula_9, pelicula_10,
                       serie_1, serie_2, serie_3, serie_4, serie_5, serie_6,
                       serie_7, serie_8, serie_9, serie_10]

"""Crea una lista con todas los titulos de las series y peliculas"""
random_sp = random.sample(lista_peliculas_series, 10)