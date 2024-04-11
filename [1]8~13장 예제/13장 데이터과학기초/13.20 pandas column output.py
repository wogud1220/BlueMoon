# 13.10 조건에 맞는 열 데이터 출력하기

import pandas as pd
pop = pd.read_csv('population.csv')
pop_high = pop[pop['population'] > 500000]
print(pop_high)
pop_gu = pop.loc[pop['population'] > 500000, 'gu']
print(pop_gu)
