import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]



x = []
y = []

def f(x):
    return 3*x+2

for i in range(0, 6):
    x.append(i)
    y2 = f(i)
    y.append(y2)

plt.plot(x, y) # oppretter et plott
plt.scatter(x, y)
plt.show() # viser plottet