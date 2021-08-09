# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 14:41:39 2021

@author: gonzalo
"""

import pandas as pd



a = pd.read_csv(r'C:\Users\gonzalo\OneDrive\Documentos\Documentos_csv\acciones_para_portfolio.csv',
                      encoding='utf-8-sig',
                      index_col="fecha",
                      delimiter=";",
                      parse_dates = True,
                      dayfirst=True)


b = a.loc[a.index > "01-01-2020",["LTM"]] 
c = a.loc[a.index > "01-01-2020",["COPEC"]] #con esta función cortamos por fecha y columnas

trozos = [c,b]
d = b.join(c)
e = b.resample("M").mean()




