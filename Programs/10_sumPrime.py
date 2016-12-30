

################################
#Project Euler

#Problem Statement 10

################################
import time
import math

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
	if (n!=3 and n!=5 and (n%3==0 or n%5==0)):
		y=0
	else:
		length=len(divisible(n))
		if (length==1):
			y=n
		else:
			y=0
	return y	
	
def sumPrime():
	#Choose a huge number	
	flag="true"
	#start from a huge number
	N=2000000
	#only odd numbers can be prime
	data=range(1,N,2)
	#print(list(data))				
	prime=list(map(checkPrime,list(data)))
	#print(prime)
	sumPrime=sum(prime)
	result=sumPrime-1+2 #in the list of prime, 1 is also considered a prime, as it deletes 2 due to optimization
	return result
		
#time for execution of script
start_time = time.time()
result=sumPrime()
print(result)
print("--- %s seconds ---" % (time.time() - start_time))


