# 13.18 엑셀 파일 읽기

import pandas as pd
import openpyxl
city = pd.read_excel('city.xlsx', sheet_name = 'city')
print(city)
