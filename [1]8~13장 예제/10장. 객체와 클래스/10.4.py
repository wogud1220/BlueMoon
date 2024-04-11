class Account:
   def __init__(self, name):
      self.__name = name
      self.__balance = 0

   def getBalance(self):
      return self.__balance 

   def deposit(self, amount):
      self.__balance += amount 
      return self.__balance
