# 13.16 판다스로 통계 정보 출력하기

import pandas as pd
pop = pd.read_csv("population.csv")
print(pop.describe())
