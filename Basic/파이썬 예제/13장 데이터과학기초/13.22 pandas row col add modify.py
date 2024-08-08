# 13.22 열과 행을 추가하고 수정하기

import pandas as pd
pop = pd.read_csv('population.csv')
pop['인구(만명)'] = pop['population']/10000
pop['population'] = pop['population']/1000
print(pop.head(10))
