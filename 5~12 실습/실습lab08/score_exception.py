class BreakException(Exception):
    def __str__(self):
        return "-1 입력입니다."
    
class InvalidException(Exception):
    def __str__(self):
        return "유효한 점수가 아닙니다. 다시 입력하세요."
    
score = []

print("점수 입력(종료: -1)")

try:
    while True:
        try:
            s = int(input())
            
            if s == -1:
                raise BreakException
            
            elif s < 0 or s > 100:
                raise InvalidException
            
            score.append(int(s))
            
        except ValueError:
            print("잘못된 입력입니다. 다시 입력하세요.")

        except InvalidException as e:
            print(e)
            
except BreakException as e:
    #print(e)
    print("최고 점수 :", max(score))
    print("최저 점수 :", min(score))
    print("합계 :", sum(score))
    print("평균 : %.2f" %(sum(score)/len(score)))





