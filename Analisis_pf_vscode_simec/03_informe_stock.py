
# %%
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd


# %%
start= '2005-05-01'
end = '2021-11-05'

# %%
time_series = pd.date_range(start, end=end, freq='D')


# %%

df = yf.download(['DNN'], start=start, end=end)
print(df.head(), df.tail())


# %%
df.info()

# %%
df_Close = df.drop(columns=['Open','High','Low','Volume', 'Adj Close'])
print(df_Close)


# %%
df_Close.plot()

# %%
oco_v = yf.Ticker('DNN')


# %%
oco_v.info

# %%

info_oco = oco_v.info
print(type(info_oco))

for dict in info_oco:
  if dict == 'recommendationKey':
    print(info_oco[dict])

# %%
oco_v.financials

# %%
oco_v.major_holders

