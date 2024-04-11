# 헤론의 공식을 이용한 삼각형 면적 계산 함수

import math
def heron(A, B, C): 
    S = (A + B + C)/2 
    area = math.sqrt(S * (S-A) * (S-B) * (S-C))
    return area

print(heron(3,4,5))
