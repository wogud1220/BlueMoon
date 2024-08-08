class Employee: # 일반 직원(Employee)
   def __init__(self, name, salary):
      self.name = name;
      self.salary = salary;

   def pay(self):
      return self.salary

class Manager(Employee): # 관리자(Manager)
   def __init__(self, name, salary, bonus):
      Employee.__init__(self, name, salary)
      self.bonus = bonus

   def pay(self):
      return self.salary + self.bonus  

   def getBonus(self):
      return self.bonus
