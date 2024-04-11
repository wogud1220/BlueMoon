class Account:
   def __init__(self, name):
      self.name = name
      self.balance = 0

   def getBalance(self):
      return self.balance

   def deposit(self, amount):
      self.balance += amount 
      return self.balance

   def withdraw(self, amount):
      if amount <= self.balance:
         self.balance -= amount
      else:
         print("잔액 부족")
      return self.balance
