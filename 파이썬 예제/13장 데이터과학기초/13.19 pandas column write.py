# 13.19 특정 열 데이터 출력하기

import pandas as pd
pop = pd.read_csv('population.csv')
gu = pop['gu']
print(gu.head())
print(gu.shape)
gu_pop= pop[['gu', 'population']]
print(gu_pop.head(10))
