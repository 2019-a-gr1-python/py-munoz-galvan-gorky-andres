#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:33:46 2019

@author: usrdel
"""

import pandas as pd
import json
import os

path = '/Users/usrdel/Documents/GitHub/py-munoz-galvan-gorky-andres/03_Pandas/data/artwork'

archivo = '/a/000/a00001-1035.json'

path_archivo = path+archivo

llaves =['id','all_artists',
         'title','medium',
         'dateText','acquisitionYear',
         'height','width','units']   


def leerJson(path, llaves):
    with open(path_archivo) as texto_json:
        contenido_json = json.load(texto_json)
    registro_df_lista =[]
    for llave in llaves:
        valor = contenido_json[llave]
        registro_df_lista.append(valor)
    return registro_df_lista

leerJson(path_archivo,llaves)
    