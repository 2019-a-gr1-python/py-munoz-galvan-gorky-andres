# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 08:05:09 2019

@author: Gorky
"""

import pandas as pd
import sqlite3

path_guardado = 'C://Users/Gorky/Documents/GitHub/py-munoz-galvan-gorky-andres/03_Pandas/data/csv/artwork_data.pickle'

## GUARDAR SQL

df = pd.read_pickle(path_guardado)

with sqlite3.connect('bdd_python.db') as conexion:
    df.to_sql('tabla',conexion)
    
df.to_json('artistas.json')
df.to_json('artistas_orientado_tabla.json',orient='table')