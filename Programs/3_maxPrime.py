
################################
#Project Euler

#Problem Statement 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

################################
import time
import math
def divisible(number):
	#obtain list of numbers, that the input number is divisible from
	listDiv=[]		
	for i in range(1,sqrtNum(number)+1):		
		if (number % i == 0 ):
			listDiv.append(i)
	return listDiv


def sqrtNum(number):
	result=int(math.sqrt(int(number)))
	return result

def checkPrime(divList):
	primeIdx=0
	l=[]
	idx=-1#index in python starts from 0
	flag=2
	for i in divList:
		#length of the integers in the list will indicate if the number is prime 
		length=len(divisible(i))
		l.append(length)
	#list of indices where the value is 1. Value of one indicates the number is prime as the list is made of 2 elements [1,the number]
	listOne=[i for i,x in enumerate(l) if x==1]		

	#max index of the listOne will be the index of the prime number with max value 			   		
	maxPrime=divList[max(listOne)]			
	return maxPrime
			
	
def maxPrime():
	number=int(input('Insert the number'))	

	#get the list of all the numbers that can divide the input
	listDiv=divisible(number)
	print(listDiv)
	#get the max prime number
	print("")
	result=checkPrime(listDiv)

	print(result)

	return result			
	

#time for execution of script
start_time = time.time()
maxPrime()
print("--- %s seconds ---" % (time.time() - start_time))


