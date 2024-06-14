# 13.23 열과 행을 삭제하기

import pandas as pd
pop = pd.read_csv('population.csv')
pop['인구(만명)'] = pop['population']/10000
pop['population'] = pop['population']/1000
print(pop.head(10))
pop.drop(['인구(만명)'], axis=1, inplace=True)
print(pop.head(10))
pop.drop(index=3, axis=0, inplace=True)
print(pop.head(10))
