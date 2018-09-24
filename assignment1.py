'''The objective of this project is to sequntially find how the data interacts with the apriori distribution to create a
   distribution that is a mixture of both the expectaitons as well as the data from the experiment.'''
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.stats import beta
import matplotlib.patches as mpatches

def init():
	'''Hard coded parameters'''
	a=4
	b=6
	sz=150
	mean=0.5
	return a,b,sz,mean

def main():
    a,b,sz,mean=init()
    results=[]
    data_points=sp.random.binomial(size=sz,n=1,p=mean)
    for data_point in data_points:
        if data_point==1:
            a+=1
        else:
            b+=1
        results+=[(a,b)]
    fig, ax = plt.subplots()
    x = np.arange(0, 1, 0.01)


    line, = ax.plot(beta.pdf(x,1,1))

    def init2():
        line.set_ydata([np.nan] * len(x))
        return line,

    def update(i):
        line.set_ydata(beta.pdf(x, results[i%len(results)][0], results[i%len(results)][1]))
        return line,

    ani = animation.FuncAnimation(fig, update, init_func = init2, interval = 300, blit = True, repeat_delay = 5000)

    plt.show()


if __name__=='__main__':
	main()
