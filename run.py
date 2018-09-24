"""
This project aims to see the difference between sequential learning and
complete learning. We work on the coin tossing problem.
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.stats import beta
import imageio


class Data:
    def __init__(self):
        self.points = []

    def generate(self, mean, numOfPoints):
        self.points = np.random.binomial(size=numOfPoints, n=1, p=mean)


data = Data()
data.generate(0.5,150)


fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01).reshape(-1,1)
#y = np.linspace(0, 2*np.pi, 120).reshape(-1,1)
line, = ax.plot(np.sin(x))

def init():
    line.set_ydata([np.nan] * len(x))
    return line,

def update(i):
    line.set_ydata(beta.pdf(x, i/2 , i/4))
    return line,

ani = animation.FuncAnimation(fig, update, init_func = init, interval = 20, blit = True)

plt.show()
