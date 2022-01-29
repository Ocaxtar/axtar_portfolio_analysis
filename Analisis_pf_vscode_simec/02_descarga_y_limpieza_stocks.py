import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd


start= '2018-11-08'
end = '2021-11-08'
file = pd.read_csv("Analsis_pf_drive\stock_list.csv")
stock_list = file.columns.values.tolist()




stock_df = yf.download(stock_list, start=start, end=end)
df = stock_df.Close

df


df_cleaned = df.dropna(axis=1, how='any')


df_2019 = df_cleaned.loc['2018-12-31'] > df_cleaned.loc['2019-12-31']
df_cleaned = df_cleaned[df_cleaned.columns[~df_2019]]
df_2020 = df_cleaned.loc['2019-12-31'] > df_cleaned.loc['2020-12-31']
df_cleaned = df_cleaned[df_cleaned.columns[~df_2020]]
df_2021 = df_cleaned.loc['2020-12-31'] > df_cleaned.loc['2021-08-31']

df_cleaned.shape


df_cleaned.to_csv("Analsis_pf_drive\stock_pf_cleaned.csv")


