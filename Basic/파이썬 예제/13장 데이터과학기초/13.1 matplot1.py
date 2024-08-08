import matplotlib.pyplot as plt
X = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Y = [0, 2, 1, 3, 2, 4, 7, 12, 15, 5]
plt.bar(X, Y)
plt.xlabel("score")
plt.ylabel("count")
plt.show()