
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools


stock_pf_cleaned= pd.read_csv("Analsis_pf_drive\stock_pf_cleaned.csv", header=0, parse_dates=[0], index_col=0)
lista = stock_pf_cleaned.columns.values.tolist()

lista_de_listas = []
for x in itertools.combinations(lista, 5):
    lista_de_listas.append(x)

stock_pf_cleaned[list(lista_de_listas[0])]



for i in lista_de_listas:
    #Construir un df con el valor de las acciones por columna y DateTimeIndex como índice
    selected_df = stock_pf_cleaned[list(2)]
    daily_returns = selected_df.pct_change() # Calcular los retornos porcentuales diarios

    #Peso de portfolio: Peso = (Valor de las acciones de una compañia / Valor total de cartera ) x 100 
    weights = np.array([0.2,0.2,0.2,0.2,0.2]) #porcentaje del peso asignado a cada activo
    # meanDailyReturns = daily_returns.mean()
    # pf_return = np.sum(meanDailyReturns*weights)
    
    cov_matrix_d = daily_returns.cov() # Construimos la matriz de covarianza para el retorno diario
    cov_matrix_a = (daily_returns.cov())*250 #Covarianza anualizada

    port_variance = np.dot(weights.T, np.dot(cov_matrix_a, weights)) # Calcula la varianza con la formula
    print(str(np.round(port_variance, 3)* 100) +'%') # imprime la varianza en formato porcentaje
    port_stddev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix_a, weights)))
    print(str(np.round(port_stddev, 3) *100) + '%') #imprime el porcentaje de desviación estandard

    daily_returns['Portfolio'] = daily_returns.dot(weights) # Creamos columna portfolio con el total de retornos
    daily_cum_ret=(1+daily_returns).cumprod() #porcentaje de retorno acumulado en el tiempo
    daily_cum_ret.Portfolio.plot() # Gráfica de retorno acumulado
    plt.show()
    # daily_returns.Portfolio.tail()

    # daily_cum_ret.head()
    daily_cum_ret.tail()

    #hasta aquí parte probada. Lo siguiente es código en pruebas
    total_return = (stock_price[-1] - stock_price[0]) / stock_price[0]

    years = 2 # total de años que tiene el df    
    total_return = (stock_price[-1] - stock_price[0]) / stock_price[0] # Calcula el retorno total
    annualized_return = ((1 + total_return)**(1/years))-1
    print(annualized_return)

    annualized_vol = stock_returns.std()*np.sqrt(250) #Calcula la desviación std anualizada
    print(annualized_vol)

    risk_free = 0.01 # Define el ratio libre de riesgo
    sharpe_ratio = (annualized_return - risk_free) / annualized_vol
    print(sharpe_ratio)

    stock_returns=stock_price.pct_change() 
    stock_returns.hist() # Imprime la distribución de retornos relativo a la normal, donde se pueden ver el reparto de retornos positivos y negativos y su diferencia con una distribución normalizada en forma de campana gauss
'''
print("mean : ", stock_returns.mean())
print("vol : ", stock_returns.std())
print("skew : ", stock_returns.skew())
print("kurt : ", stock_returns.kurtosis())

target_return = 0
negative_returns = df.loc[df['stock'] < 0] # devuelve los retornos negativos de un stock

expected_return = df['stock'].mean() #Calcula retorno medio
down_stddev = negative_returns.std() #Calcula std dev de retornos negativos
sortino_ratio = (expected_return - risk_free) / down_stddev #Calcula el Sortino ratio - ratio de draw-down
print(sortino_ratio)

roll_max = stock_price.rolling(min_periods=1, window=250).max() # Calcula el máximo valor de retornos anualizado usando rolling().max()
daily_drawdown = stock_price/roll_max - 1.0 #Calcula draw-down diario de maximo rolling
max_daily_drawdown = daily_drawdown.rolling(min_periods=1, window=250).max() #Calcula mínimo draw-down anualizado  - consultar posible error min / max
daily_drawdown.plot()
max_daily_drawdown.plot()
plt.show()
'''



'''
Parte 3
# Crear un df_pf con los stocks como filas y columnas: mean_ret //retorno medio, var ,pf_w //peso sectorial del portfolio, bm_w //peso sectorial del benchmark, Sector // Sector al que pertenece el activo, investigar la sectorización más estandarizada, GICS o ICB
https://www.ftserussell.com/data/industry-classification-benchmark-icb

total_return_pf = (pf_w*mean_ret).sum() #Calcula retorno medio del portfolio
total_return_bm = (bm_w*mean_ret).sum() #Calcula retorno medio del benchmark
active_return = total_return_pf - total_return_bm #Diferencia
print(active_return)

grouped_df=df_pf.groupby('Sector').sum() #Grupaje por sector
grouped_df['active_weight']=grouped_df['pf_w']-grouped_df['bm_w'] #Calcula el peso activo por sector
print(grouped_df['active_weight'])

Risk Factors //Revisar

P

'''


