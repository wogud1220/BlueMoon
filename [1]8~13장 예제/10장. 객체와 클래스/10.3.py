class Account:
   counter = 0 
   def __init__(self, myname):
      self.name = myname
      self.balance = 0
      Account.counter += 1

   def __del__(self):
      Account.counter -= 1

   def getCounter(self):
      return Account.counter
