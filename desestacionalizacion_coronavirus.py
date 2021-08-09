# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:45:11 2021

@author: gonzalo
"""

import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

a = pd.read_csv(r'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto5/TotalesNacionales_T.csv',
                      encoding='utf-8-sig',
                      index_col=0,
                      delimiter=",",
                      parse_dates = True,
                      decimal='.',
                      dayfirst=True)

nuevos = a['Casos nuevos totales']


s = seasonal_decompose(nuevos)
#s.plot()
s.trend.plot()

