import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



stock_pf_cleaned= pd.read_csv("Analsis_pf_drive\stock_pf_cleaned.csv", header=0, parse_dates=[0], index_col=0)
lista = [ACLS, AMAT, AMD, ASML]

def analisis_pf (lista):
    #Construir un df con el valor de las acciones por columna y DateTimeIndex como índice
    selected_df = stock_pf_cleaned.loc[:,lista]
    # print(selected_df.info())
    daily_returns = selected_df.pct_change() # Calcular los retornos diarios 
    weights = np.array([0.25,0.25,0.25,0.25]) #porcentaje del peso asignado a cada activo
    meanDailyReturns = daily_returns.mean()
    pf_return = np.sum(meanDailyReturns*weights)

    #Peso de portfolio: Peso = (Valor de las acciones de una compañia / Valor total de cartera ) x 100
    cov_matrix_d = daily_returns.cov() # Construimos la matriz de covarianza para el retorno diario
    cov_matrix_a = (daily_returns.cov())*250 #Covarianza anualizada

    port_variance = np.dot(weights.T, np.dot(cov_matrix_a, weights)) # Calcula la varianza con la formula
    print(str(np.round(port_variance, 3)* 100) +'% varianza') # imprime la varianza en formato porcentaje

    port_stddev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix_a, weights)))
    print(str(np.round(port_stddev, 3) *100) + '% desviacion estandard') #imprime el porcentaje de desviación estandard

    daily_returns['Portfolio'] = daily_returns.dot(weights) # Creamos columna portfolio con el total de retornos

    daily_cum_ret=(1+daily_returns).cumprod() #porcentaje de retorno acumulado en el tiempo
    # daily_cum_ret.Portfolio.plot() # Gráfica de retorno acumulado
    daily_returns.Portfolio.tail()

    daily_cum_ret.head()
    daily_cum_ret.tail()


