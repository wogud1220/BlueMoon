
























'''
import numpy as np

first = np.arange(10, 20)
second = np.arange(1, 10)

for i in range (0, first.size):
    print(first[i]*second)
'''

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

scores = [[90, 70, 85], 
         [95, 88, 80],
         [65, 75, 85],
         [90, 92, 100]]
student = ['찬호','승엽','연아','지연']
score = np.array(scores) 
print(score)
student_mean = np.mean(score, axis = 1)
subject_mean = np.mean(score, axis = 0)
subject_max = np.amax(score, axis = 0)
print('student_mean', student_mean)
print('subject_mean', subject_mean)
print('subject_max', subject_max)

plt.bar(student, student_mean)
plt.show()
