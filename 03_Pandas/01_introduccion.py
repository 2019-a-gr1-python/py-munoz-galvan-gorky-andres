#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:40:39 2019

@author: usrdel
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

numeros_serie_a = pd.Series(lista_numeros)
numeros_serie_b = pd.Series(tupla_numeros)
numeros_serie_c = pd.Series(np_numeros)
numeros_serie_d = pd.Series([
        True,
        False,
        12,
        12.21,
        "Asad",
        None,
        (),
        [],
        {"nombre":"Adrian"}])

numeros_serie_a[0]

lista_ciudades = ["Ambato","Cuenca","Loja",
                  "Quito"]

serie_ciudades = pd.Series(lista_ciudades,
                           index=["A","C","L",
                                  "Q"])
serie_ciudades["Q"]
serie_ciudades[0]
serie_ciudades[1]
serie_ciudades[2]
serie_ciudades[3]

print(type(serie_ciudades))

# CONCATENAR SERIES
# añadir un indice valor a una serie
# Máximo
# Mínimo
# Estadísticas (Avg Mean ...)

serie_ciudades.add("AA")