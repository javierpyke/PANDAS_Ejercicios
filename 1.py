import pandas as pd 
import numpy as np

# Cargar base de datos imdb de titulos de peliculas
titulos = pd.read_csv('titles.csv')

# Cargar base de datos de elenco de peliculas, de imdb
cast = pd.read_csv('cast.csv')

# Cuantas peliculas estan listadas en el dataframe de titulos?
#   print('Hay {} peliculas.'.format(titulos['title'].count()))
#   print('--------------------------------------------------')

# Cuales son las peliculas mas antiguas listadas en titulos?
print(titulos.sort_values(by='year').head(10))
print('--------------------------------------------------')

# Cuantas peliculas estan listadas por el nombre "Dracula" ?
print(titulos[titulos['title'] == 'Dracula'].count())
print('--------------------------------------------------')

# Titulos mas comunes en la historia filmografica
cant_titulos = titulos.groupby('title').count()
cant_titulos = cant_titulos.rename(columns={'year':'cant'})
print(cant_titulos.sort_values(by='cant',ascending=False))
print('--------------------------------------------------')
# Cual fue la primer pelicula hecha titulada "Romeo and Juliet" ?
print(titulos[titulos['title'] == 'Romeo and Juliet'].sort_values(by='year').head(1))
print('--------------------------------------------------')
# Listar todas las peliculas que contengan la palabra "Exorcist"
	# ordenadas de la mas vieja a la mas reciente.
print(titulos[titulos['title'].str.contains('Exorcist')].sort_values(by='year'))
print('--------------------------------------------------')
# Cuantas peliculas fueron hechas en el año 1950?
print('Fueron hechas {} peliculas en 1950.'.format(titulos[titulos['year'] == 1950].count()['year']))
print('--------------------------------------------------')
# Cuantas peliculas fueron hechas en el año 1970?
print('Fueron hechas {} peliculas en 1970.'.format(titulos[titulos['year'] == 1970].count()['year']))
print('--------------------------------------------------')
# Cuantas peliculas fueron hechas de 1950 a 1959
print('Fueron hechas {} peliculas desde 1950 a 1959.'.format(titulos[(titulos['year']>=1950) & (titulos['year']<=1959)].count()['year']))
print('--------------------------------------------------')
# En que años alguna pelicula llamada "Batman" se presento
print(titulos[titulos['title']=='Batman']['year'])
print('--------------------------------------------------')
# Cuantos roles o papeles hubo en la pelicula "The Godfather"
print('En The Godfather hubo {} roles.'.format(cast[cast['title']=='The Godfather'].count()['title']))
print('--------------------------------------------------')
# Cuantos papeles en la pelicula "The Godfather" no estan clasificados en algun valor "n"
print('En The Godfather hubo {} roles que no estan clasificados en algun valor "n".'.format(cast[(cast['title']=='The Godfather') & (cast['n'].isnull())].count()['title']))
print('--------------------------------------------------')
# Mostrar el elenco completo de la pelicula "2001: A Space Odyssey" 
	# ordenado por su clasificasión "n", ignorando los papeles que 
	# no se les asigno ningun valor "n"
print(cast[(cast['title']=='2001: A Space Odyssey') & (cast['n'].notnull())].sort_values(by='n',ascending=False))
print('--------------------------------------------------')
# Mostrar el elenco completo ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958
print(cast[(cast['title']=='Dracula') & (cast['year']==1958)].sort_values(by='n',ascending=False))
print('--------------------------------------------------')
# Cuantos papeles fueron listados en la pelicula "The Wizard of Oz" de 1939
print(cast[(cast['title']=='The Wizard of Oz') & (cast['year']==1939)].count()['name'])
print('--------------------------------------------------')
# Cuantos papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas
print(cast[cast['character']=='Bruce Wayne'].count()['character'])
print('--------------------------------------------------')
# Cuanta gente ha hecho el papel de "Romeo"
print(cast[cast['character']=='Romeo'].count()['character'])
print('--------------------------------------------------')
# Cuantos papeles ha hecho "Robert De Niro" en su carrera
print(cast[cast['name']=='Robert De Niro'].count()['name'])
print('--------------------------------------------------')
# Listado de papeles de soporte que tuvo el actor "Charlton Heston" en la decada de los 50's, ordenado por año
print(cast[(cast['name']=='Charlton Heston') & (cast['year']//10 == 195) & (cast['n']==2.0)].sort_values('year'))
print('--------------------------------------------------')
# Listado de papeles como protagonista que tuvo el actor "Charlton Heston" en
	# la decada de los 60's, ordenado por año de forma descendente
print(cast[(cast['name']=='Charlton Heston') & (cast['year']//10 == 196) & (cast['n']==1.0)].sort_values('year',ascending=False))
print('--------------------------------------------------')
# ¿Cuantos papeles para actores hubo en la decada de los 50's?
print(cast[(cast['type']=='actor') & (cast['year']//10 == 195)].count()['type'])
print('--------------------------------------------------')
# ¿Cuantos papeles para actrices hubo en la decada de los 50's ?
print(cast[(cast['type']=='actress') & (cast['year']//10 == 195)].count()['type'])
print('--------------------------------------------------')
# ¿Cuantos papeles protagonicos existen desde el principio de la historia filmatografica hasta 1970 ?
print(cast[(cast['year']<1970) & (cast['n']==1.0)].count()['n'])