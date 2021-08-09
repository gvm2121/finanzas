# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:52:27 2021

@author: gonzalo
"""

import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
coronavirus_por_comuna = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19_T.csv"


a = pd.read_csv(coronavirus_por_comuna,
                      encoding='utf-8-sig',
                      index_col=0,
                      delimiter=",",
                      parse_dates = True,
                      decimal='.',
                      dayfirst=True)

print(a)

