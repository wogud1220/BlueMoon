# 13.21 특정 열 정렬하기

import pandas as pd
pop = pd.read_csv('population.csv')
result = pop.sort_values(by = "population")
print(result)
result = pop.sort_values(by = "population", ascending = False).head(10)
print(result)
result = pop.sort_values(by = "density", ascending = False).head()
print(result)
