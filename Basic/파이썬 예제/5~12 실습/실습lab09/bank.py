class Account():
    def __init__(self, name, number, ini_bal):
        self.__owner = name
        self.__number = number
        self.__balance = ini_bal
        self.__history = []
        self.__history.append(("신규", ini_bal, self.__balance))
    
    def deposit(self, amount):
        self.__balance += amount
        print("%d원이 입금되었습니다." %amount)
        self.__history.append(("입금", amount, self.__balance))

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("%d원이 출금되었습니다." %amount)
            self.__history.append(("출금", amount, self.__balance))
        else:
            print("잔액이 부족합니다.")
            
    def __str__(self):
        msg = "계좌번호 : "+str(self.__number)+" , 소유자 : "+str(self.__owner) + " , 잔액 = "+ str(self.__balance)
        return msg
    
    def print_history(self):
        print("계좌번호 : "+str(self.__number)+" , 소유자 : "+str(self.__owner))
        
        for transaction, amount, balance in self.__history:
            print("%s %10d 원" %(transaction, amount), end='\t')
            print("잔액 %10d 원" %balance)


# 전체 계좌 딕셔너리 (계좌번호string - 객체)
acc_list = {}
         
def find_account():
    if not acc_list:
        print("생성된 계좌가 없습니다")
        return False
    
    num = input("계좌 번호를 입력하세요 : ")
    if num in acc_list:
        return acc_list[num]
    
    print("해당 계좌가 없습니다")
    return False
                  
def print_menu():
    print('='*40)
    print("          SOOKMYUNG BANK ATM")
    print('='*40)
    print("1. 신규 계좌 생성")
    print("2. 잔액 조회")
    print("3. 입금")
    print("4. 출금")
    print("5. 거래 내역 조회")
    print("6. 종료")
    print('-'*40)


while True:
    print_menu()
    select = int(input("선택 : "))
    
    if select == 1:
        name = input("계좌 소유자 이름을 입력하세요: ")
        number = input("생성할 계좌 번호를 입력하세요: ")
        while number in acc_list:
            print("사용할 수 없는 계좌 번호입니다. 다시 입력하세요.")
            number = input("생성할 계좌 번호를 입력하세요: ")
            
        amount = int(input("입금할 금액을 입력하세요 : "))
        account = Account(name, number, amount)
        acc_list[number] = account
        print()
        print("[ 생성된 계좌 정보 ]")
        print(account) 
        
    elif select == 2:
        account = find_account()
        if account:
            print(account)
                         
    elif select == 3:
        account = find_account()
        if account:
            amount = int(input("입금하실 금액을 입력하세요 : "))
            account.deposit(amount)
                  
    elif select == 4:
        account = find_account()
        if account:
            amount = int(input("출금하실 금액을 입력하세요 : "))
            account.withdraw(amount)
        
    elif select == 5:
        account = find_account()
        if account:
            account.print_history()
        
    elif select == 6:
        print("\n이용해주셔서 감사합니다.")
        break
        
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")

    print()
