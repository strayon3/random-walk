import numpy as np
import random
from matplotlib import pyplot as plt

# creat variables
steps = 100
p = 0.5

# create walk function


def Randomwalk(Ns, p, line):
    # creat an array for the  steps initi it to zero
    postion = np.empty(Ns)
    postion[0] = 0
    pos_counter = 0
# creat an array for max steps generate random probablity
    max_steps = np.arange(Ns)
# for lopp to start the walk
    for i in range(1, Ns):
        # creat if else statment to add or subtract the counter
        test = random.random()
        if test >= p:
            pos_counter += 1
        else:
            pos_counter -= 1
# make postion array = to the counter
        postion[i] = pos_counter

# genertae plot of walked pos
    plt.plot(max_steps, postion, line)
    plt.xlabel('Steps Taken')
    plt.ylabel('Distance From start')
    return None


# create new figureto plot walk
plt.figure

# function callback
Randomwalk(steps, p, line='o--')
# hold the first random walk

# show both random walks on the plot
Randomwalk(steps, p, line='-')
plt.show()
