class Person:
   def sleep(self):
      print('잠을 잡니다.')

class Student(Person):
   def study(self):
      print('공부합니다.')
   def play(self):
      print('친구와 놉니다.')

class Worker(Person):
   def work(self):
      print('일합니다.')
   def play(self):
      print('술을 마십니다.')
      
class Arbeit(Student, Worker): 
   def myjob(self):
      print('나는 알바 학생입니다:')
      self.sleep()
      self.play()
      self.study()
      self.work()
