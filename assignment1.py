'''The objective of this project is to sequntially find how the data interacts with the apriori distribution to create a 
   distribution that is a mixture of both the expectaitons as well as the data from the experiment.'''
import scipy as sp
import numpy as np

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
		results+=[np.random.beta(a,b)]
	
	print(results)
	
if __name__=='__main__':
	main()
