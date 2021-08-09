# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 12:51:33 2021

@author: gonzalo
"""

import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.scimath import sqrt
#usando ecuacion 3 pagina 8 Expectativas Financieras
#y Tasas Forward en Chile Rodrigo Alfaro
#Antonio Fernandois
#Andrés Sagner
#N.º 814 Marzo 2018

def funcion_matriz_epsilon(la):
    matriz_epsilon_y = np.array([
        [1, (1-np.exp(-1*la)/1*la),((1-np.exp((-1*la))/1*la)-np.exp(-1*la))],
        [1, (1-np.exp((-2*la))/2*la),((1-np.exp((-2*la))/2*la)-np.exp(-2*la))],
        [1, (1-np.exp((-3*la))/3*la),((1-np.exp((-3*la))/3*la)-np.exp(-3*la))],
        [1, (1-np.exp((-24*la))/24*la),((1-np.exp((-24*la))/24*la)-np.exp(-24*la))],
        [1, (1-np.exp((-60*la))/60*la),((1-np.exp((-60*la))/60*la)-np.exp(-60*la))],
        [1, (1-np.exp((-120*la))/120*la),((1-np.exp((-120*la))/120*la)-np.exp(-120*la))],
        ])
    return matriz_epsilon_y
vector_tasas_x = np.array([.0005,.0005,.0005,0.0229,0.0356,0.0447], ndmin=1)

#tasas bonos largos https://si3.bcentral.cl/Siete/ES/Siete/Cuadro/CAP_TASA_INTERES/MN_TASA_INTERES_09/TMS_15/T311
registro = []
RECM_GUARDADO = 1
MINIMO_TAU = 1
for a in range(9,109):
    b=a/1000
    linea = []
    modelo = sm.OLS(vector_tasas_x,funcion_matriz_epsilon(b)).fit()
    betas = modelo.params
    residuales = modelo.resid
    vector_tasas_modelo = np.dot(funcion_matriz_epsilon(b),betas)


    #calculo de RECM
    recm_array = (vector_tasas_x - vector_tasas_modelo)**2
    filas = recm_array.shape
    recm = sqrt(recm_array.sum()/filas)
    
    #menor recm
    if recm < RECM_GUARDADO:
        RECM_GUARDADO = recm
        MINIMO_TAU = b
        
        
    linea.append(b)
    linea.append(recm)
    registro.append(linea)
print(RECM_GUARDADO)
print(MINIMO_TAU)


#modelo nelson siegel
#coeficientes

def coeficientes_ns(plazo,la):
    return np.array([1, (1-np.exp(-plazo*la)/plazo*la),((1-np.exp((-plazo*la))/plazo*la)-np.exp(-plazo*la))])

modelo = sm.OLS(vector_tasas_x,funcion_matriz_epsilon(MINIMO_TAU)).fit()
ns_modelo = np.empty((0,2))
for i in range(1,121):
    ns = np.dot(coeficientes_ns(i,MINIMO_TAU),np.array(modelo.params,ndmin=1))
    ns_modelo = np.append(ns_modelo,np.array([[i,ns]]), axis=0)


#los plazos abajo son en función de las tasas vistas en el mercado
grafico,ax = plt.subplots()

ax.scatter(np.array([1,2,3,24,60,120],ndmin=1),vector_tasas_x,label="Observado",color='r')
ax.plot(ns_modelo[:,0],ns_modelo[:,1],label="Nelson Siegel")
ax.set_title("Nelson Siegel")
ax.set_xlabel("Meses")
ax.set_ylabel("Tasa")

ax.legend()






