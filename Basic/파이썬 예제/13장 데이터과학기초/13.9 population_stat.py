# 13.9 인구 통계 그래프 그리기

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
gu = ['강남', '강동', '강서', '관악', '구로', '노원', '동작', '마포', '서초', '성북', '송파', '양천', '영등포',  '용산', '은평']
population = [550209, 440390, 598273, 517334, 439371, 537303, 408912, 385925, 435107, 454744, 682741, 462285, 400986, 245185, 484546]
area = [39.5, 24.59, 41.44, 29.57, 20.12, 35.44, 16.35, 23.85, 46.98, 24.57, 33.87, 17.41, 24.55, 21.87, 29.71]
np_gu = np.array(gu)
np_population = np.array(population)
np_area = np.array(area)
np_density = np_population / np_area
plt.bar(np_gu, np_population)
plt.ylabel("인구 (명)")
plt.show()
