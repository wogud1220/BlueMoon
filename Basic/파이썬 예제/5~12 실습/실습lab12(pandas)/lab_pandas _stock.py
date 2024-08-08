# 13.21 특정 열 정렬하기

import pandas as pd
#pd.set_option('display.max_columns', None)
pd.options.display.max_columns = 10
pd.set_option('display.width', 1000)

stock = pd.read_csv('stock.csv')
print(stock)
print()
print('delete row 22')
stock.drop(index=22, axis = 0, inplace= True)
print(stock.tail(5))

print()
print('add row to index 22')
item = ['XOM','EXXON MOBIL CORPORATION',97.59, 25588794, 411102100000, 16.0, 97.9300]
stock.loc[22]=item
print(stock.tail(5))
'''
print("Market cap sort")
result = stock.sort_values(by = "Market cap", ascending = False).head(10)
print(result)
'''
print()
print("Volume sort")
result = stock.sort_values(by = "Volume", ascending = False).head(10)
print(result[['Symbol','Volume']])


print()
print("52 high ratio Col. Creation")
high_52 = stock['52_high']
price = stock['Price']
stock['52_high(%)'] = (price-high_52)/high_52

result = stock.sort_values(by = '52_high(%)', ascending = False)
print (result[['Symbol', 'Price', '52_high', '52_high(%)']].head(10))
                           
print()
print("P/E ratio, less than 20, Price Drop less than 15%")
pe20 = stock[stock['P/E'] < 20]
result = pe20[pe20['52_high(%)'] >= -0.15]
print(result)

print()
print("Vol over 25M, Price less than 150")
vol_20M = stock.loc[stock['Volume'] > 2000000 , 'Symbol']
print(vol_20M)
#result = vol_20M[vol_20M['Price'] < 150]
#print(result)
