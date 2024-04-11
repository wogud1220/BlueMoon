import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Y2011 = [9, 29, 15, 110, 53, 405, 1131, 167, 26, 32, 56, 7]
Y2020 = [61, 53, 16, 17, 112, 40, 270, 676, 182, 0, 120, 5]


plt.plot(X, Y2011, label="2011")
plt.plot(X, Y2020, label="2020")
#plt.bar(X, Y2011, X, Y2020) #, label="2011")
#plt.bar(X, Y2020, label="2020")
plt.xlabel("Month")
plt.ylabel("Precipitation(mm)")
plt.legend(loc="upper right")
plt.title("Precipitations in Seoul")
plt.show()
