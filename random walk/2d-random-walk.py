from matplotlib import lines
import numpy as np
import matplotlib.pyplot as plt
import random 

steps = 100000

#set prob for x and y
x = np.zeros(steps)
y = np.zeros(steps)

for i in range (1,steps):
    value = random.randint(1,4)
    if value == 1:
        x[i] = x[i-1]+1
        y[i] = y[i - 1]
    elif value ==2:
        x[i] = x[i-1]-1
        y[i]= y[i-1]
    elif value == 3:
        x[i] = x[i-1]
        y[i] = y[i-1]+1
    else:
        x[i] = x[i-1]
        y[i] = y[i-1]-1
plt.plot(x,y)
plt.figure()
plt.show()