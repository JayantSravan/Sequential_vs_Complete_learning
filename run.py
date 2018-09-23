"""
This project aims to see the difference between sequential learning and
complete learning. We work on the coin tossing problem.
"""
import numpy as np
import scipy as sp
import matplotlib

class Data:
    def __init__(self):
        self.points = []

    def generate(self, mean, numOfPoints):
        self.points = np.random.binomial(size=numOfPoints, n=1, p=mean)


data = Data()
data.generate(0.5,150)
