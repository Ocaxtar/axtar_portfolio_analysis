from bs4 import BeautifulSoup
import requests
import csv 
import pandas as pd

symbols =[]
names=[]
prices=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]

entries = []
for i in range(0,12):
  r = requests.get("https://finance.yahoo.com/screener/predefined/growth_technology_stocks", params={'offset': str(i*25)}, headers='')
  data = BeautifulSoup(r.text).find_all('tr')
  entries.extend(data)
 
for list in entries:
  print(list)

for listing in entries:
   for symbol in listing.find_all('td', attrs={'aria-label':'Symbol'}):
      symbols.append(symbol.text)
   for name in listing.find_all('td', attrs={'aria-label':'Name'}):
      names.append(name.text)
   for price in listing.find_all('td', attrs={'aria-label':'Price (Intraday)'}):
      prices.append(price.text)
   for change in listing.find_all('td', attrs={'aria-label':'Change'}):
      changes.append(change.text)
   for percentChange in listing.find_all('td', attrs={'aria-label':'% Change'}):
      percentChanges.append(percentChange.text)
   for marketCap in listing.find_all('td', attrs={'aria-label':'Market Cap'}):
      marketCaps.append(marketCap.text)
   for totalVolume in listing.find_all('td', attrs={'aria-label':'Avg Vol (3 month)'}):
      totalVolumes.append(totalVolume.text)
   for circulatingSupply in listing.find_all('td', attrs={'aria-label':'Volume'}):
      circulatingSupplys.append(circulatingSupply.text)

lista_limpia = []
for element in symbols:
   if element not in lista_limpia:
      lista_limpia.append(element)

print(lista_limpia)
len(lista_limpia)

'''"Market Cap": marketCaps,''' 
a = {"Symbols": symbols, "Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges, 'Market Cap': marketCaps, "Average Volume": totalVolumes,"Volume":circulatingSupplys}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
df = df.drop_duplicates()
df.shape

with open("Analsis_pf_drive\grow_tech_stock_list.csv", 'w', newline='') as file:
  wr = csv.writer(file, quoting=csv.QUOTE_ALL)
  wr.writerow(symbols)
