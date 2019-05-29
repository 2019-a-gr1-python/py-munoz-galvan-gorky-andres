#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:35:42 2019

@author: usrdel
"""

import pandas as pd

path_guardado = '/Users/usrdel/Documents/GitHub/py-munoz-galvan-gorky-andres/03_Pandas/data/csv/artwork_data.pickle'

df = pd.read_pickle(path_guardado)

primero = df.loc[1035,'artist']
segundo = df.loc[1036,'units']

df.loc[0] #Error porque no esta dentro del labe indice

primero_a = df.iloc[0]['artist']
primero_a1 = df.iloc[0][1]

primero_b = df.iloc[0,:]

primero_c = df.iloc[0:100,0:2]

diez_primeros = df.head(10)['width'].sort_values()
tres_primeros = df.head(10)['width'].sort_values(ascending = False).head(3)
diez_ultimos = df.tail(10)['width'].sort_values()
tres_ultimos = df.tail(10)['width'].sort_values().tail(3)
a = df['year'].sort_values()

serie_validado = pd.to_numeric(df['width'],errors='coerce')


df.loc[:,'width'] = serie_validado
df.loc[:,5] = serie_validado #Se transforma todos a un entero

diez_primeros = df['width'].sort_values(ascending = False).head(10)
diez_ultimos = df['width'].sort_values(ascending = False).tail(10)

serie_validado_height = pd.to_numeric(df['height'],errors='coerce')
df.loc[:,'height'] = serie_validado_height

area = df['height'] * df['width']

type(area)

#Agregar una nueva columna
df['area'] = area

df = df.assign(areados = area)

df_area = df['area'].sort_values(ascending = False).head(1)

id_max_area = df['area'].idxmax()

id_min_area = df['area'].idxmin()

resgistro_mas_area = df.loc[id_max_area]

registro_menor_area = df.loc[id_min_area]

