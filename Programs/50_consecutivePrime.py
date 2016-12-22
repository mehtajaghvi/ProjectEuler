
################################
#Project Euler

#Problem Statement 50

#Consecutive prime sum
#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#Which prime, below one-million, can be written as the sum of the most consecutive primes?

################################
import time
import math
from functools import reduce

			
def sqrtNum(number):
	result=int(math.sqrt(int(number)))
	return result

def divisible(number):
	#obtain list of numbers, that the input number is divisible from
	listDiv=[]		
	for i in range(1,sqrtNum(number)+1):		
		if (number % i == 0 ):
			listDiv.append(i)
	return listDiv

def checkPrime(n):	
	#length of the integers in the list will indicate if the number is prime 
	length=len(divisible(n))
	if (length==1):
		y=n
	else:
		y=0
	return y
def consecutiveSum(listPrime):
	
	return sumC		
def consPrime():
		
	flag="true"

	N=3
	sumP=0
	while(sumP<=1500):
		
		
		data=range(1,N)				
		rawPrime=list(map(checkPrime,list(data)))
					
		sumP=sum(rawPrime)
		sumP=sumP-1
		if(sumP>=1500):
			result=N
			break
		N=N+1	
	
	print("Answer is ",result)	
		
		
			
		
				
#time for execution of script
start_time = time.time()
consPrime()
#d=checkPrime(953)

print("--- %s seconds ---" % (time.time() - start_time))
			



