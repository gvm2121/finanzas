# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:06:20 2021

@author: gonzalo
"""

import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose




a = pd.read_csv(r'C:\Users\gonzalo\OneDrive\Documentos\Documentos_csv\PIB_estacionalizado.csv',
                      encoding='utf-8-sig',
                      header=0,
                      names=['fecha','pib'],
                      index_col=0,
                      delimiter=";",
                      parse_dates = True,
                      thousands='.',
                      decimal=',',
                      dayfirst=True)


s = seasonal_decompose(a)
#aca falta transformar index como tipo tiempo y ver la fecha de cómo entra a traves del csv
#el formato MMM-YYYY no sirve