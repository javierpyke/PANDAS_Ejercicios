import pandas as pd 
import numpy as np

# Cargar base de datos imdb de titulos de peliculas
titulos = pd.read_csv('titles.csv')

# Cargar base de datos de elenco de peliculas, de imdb
cast = pd.read_csv('cast.csv')
# Cargar nuestra base de datos de elencos
df_elencos = pd.read_csv('cast.csv')
print(df_elencos)
# Ahora tambien cargaremos datos de otra base de datos
df_peliculas = pd.read_csv('titles.csv')
print(df_peliculas)
# Que tal si cargamos esta base de datos pero la columna date la convertirmos a un 
# formato datetime que tiene metodos para hacer operaciones sobre fechas.. Mejor!
df_dates = df_peliculas = pd.read_csv('release_dates.csv')
df_dates['date'] = pd.to_datetime(df_dates['date'])
print(df_dates.dtypes)

df_dates['ones'] = 1
print(df_dates)

# Con esto que podemos hacer un listado categorizando por algun elemento de la 
# fecha como por ejemplo:
# En que meses se lanzan mas comunmente peliculas que contienen la palabra
# "horror"
df_dates['meses'] = df_dates['date'].dt.month
print(df_dates)

print(df_dates[df_dates['title'].str.contains('horror',case=False)].groupby('meses')[['ones']].sum())

# Exploremos la funcionalidad para unir dataframes con el metodo "merge"
# Nos interesa conocer la fecha de lanzamiento de las peliculas en la que ah participado 
# Denzel Washington.. Pero esa información esta en otro dataframe!!

df_dates['year'] = df_dates['date'].dt.year
print(pd.merge(df_elencos[df_elencos['name']=='Denzel Washington'],df_dates[['title','year','date']][df_dates['country']=='USA'],how='left',on=['title','year']))

# Ejemplo fechas de lanzamiento de peliculas Harry Potter en Mexico, USA y Canada

df_harry = df_dates[(df_dates['title'].str.contains('Harry Potter',case=False)) &
        ((df_dates['country']=='Mexico') | (df_dates['country']=='USA') | (df_dates['country']=='Canada'))]
print(df_harry.pivot(values='date',columns='country',index='title'))

# En que fechas fue lanzada cada pelicula de "Salma Hayek"
# dentro de un periodo de 1990 al presente en Mexico

filtro1 = (df_elencos['name']=='Salma Hayek') & (df_elencos['year'] >=1990)
print(pd.merge(df_elencos[filtro1],df_dates[df_dates['country']=='Mexico'])[['title','date']])

# En que dia de la semana se han lanzado en USA las peliculas de 
# donde aparece Tom Cuise.. Incluir un grafico
# df_dates['date'].dt.day_name()
filtro2 = df_elencos['name']=='Tom Cruise'
df_tomcruise = pd.merge(df_elencos[filtro2],df_dates[df_dates['country']=='USA'])[['title','date']]
df_tomcruise['day'] = df_tomcruise['date'].dt.day_name()
print(df_tomcruise.groupby('day').count().plot(kind='bar'))

# Que peliculas han sido lanzadas en la mayor cantidad de 
# paises , incluir en un grafico las 5 mayores

df_dates.groupby('title').count().sort_values('country',ascending=False).head(5)['country'].plot(kind='bar')

# Quien tiende a ser el actor si clasificado (n > 1) que mas a 
# participado en peliculas donde el protagonista es
# Leonardo DiCaprio

pd.merge(df_elencos[(df_elencos['name']=='Leonardo DiCaprio') & (df_elencos['n']==1)][['title']],df_elencos[df_elencos['name']!='Leonardo DiCaprio'],how='inner',on='title').groupby('name').count().sort_values(by='n',ascending=False).head(1)"""