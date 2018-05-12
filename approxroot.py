#Approximates sqaure root vs the real square root
import math


def approxRoot(n,m): #n is the new number, m is the previous largest perfect root
	fac = m ** 2
	if n == (m + 1) ** 2:
		m +=1
		approx = m 
	else:
		approx = m + ((n-fac)/(2*m))
	return (approx,m)

	
#create two lists

approxList = []
rootList =[]

m = 1

for N in range(2,100):
	l,m = approxRoot(N,m)
	print('Approx = ',l)
	realRoot = math.sqrt(N)
	print('Real root= ',realRoot)