class NegativeInputException(Exception):
    pass

def input_total( ):
    try: 
        total = 0
        while True:
            try:
                score = int(input( ))   
                if score < 0 :  
                    raise NegativeInputException
                total = total + score
            except ValueError: 		  
                print('입력한 값은 정수가 아닙니다. 다시 입력해 주세요')

    except NegativeInputException as e:
        print(e) 
        return total

input_total()
