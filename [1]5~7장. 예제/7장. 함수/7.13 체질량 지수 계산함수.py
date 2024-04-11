# 키와 몸무게 리스트를 받아 체질량 지수 리스트를 계산하는 함수

# 체질량지수 계산 함수 
def bmi(height, weight):
    return weight / (height/100 * height/100)

# 키와 몸무게 리스트를 받아 체질량지수 리스트를 계산하는 함수 
def bmilist(height_weight_list) :
    list = []
    for h, w in height_weight_list:
        list.append(bmi(h,w))
    return list

list1 = [(160,52), (162,65), (170,60), (157,50), (165,48)]
result = bmilist(list1)
print(result)