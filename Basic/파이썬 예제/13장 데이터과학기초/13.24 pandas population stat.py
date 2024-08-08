# 13.24 서울시 인구 통계 정보 출력하기

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
pop = pd.read_csv('c:/python39/population.csv')
print("mean")
print("population", pop['population'].mean())
print("area", pop['area'].mean())
print("density", pop['density'].mean())
print("median")
print("population", pop['population'].median())
print("area", pop['area'].median())
print("density", pop['density'].median())
pop['location'] = [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(pop)
print(pop.groupby('location').mean())
print(pop['location'].value_counts())
pop.plot(kind = 'bar', x = 'gu', y = 'population', color = 'orange')
plt.show()
