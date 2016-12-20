
################################
#Project Euler

#Problem Statement 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

################################
import time

multiple1=3
multiple2=5
global sumN

def one_divN():
	sumN=0
	inputN=input('Input the narutal number')
	for i in range(1,int(inputN)):
		if i%multiple1==0 or i%multiple2==0:
			sumN=sumN+i
	print('The sum of natural numbers is =',sumN)
	return sumN

start_time = time.time()
one_divN()

print("--- %s seconds ---" % (time.time() - start_time))

