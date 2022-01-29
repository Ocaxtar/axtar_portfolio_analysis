
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import itertools


lista_stocks = pd.read_csv("Analsis_pf_drive\grow_tech_stock_list.csv", header=0, parse_dates=[0], index_col=0)
print(lista_stocks)





lista_de_listas = []
for x in itertools.combinations(lista_stocks, 7):
    lista_de_listas.append(x)

print(lista_de_listas)





