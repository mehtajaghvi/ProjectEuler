

################################
#Project Euler

#Problem Statement n
#10001st prime
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?
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
	length=len(divisible(n))
	if (length==1):
		y=n
	else:
		y=0
	return y	
	
def thousandPrime():
	#Choose a huge number	
	flag="true"
	#start from a huge number
	N=104700
	while(flag=="true"):
		data=range(1,N)				
		prime=list(map(checkPrime,list(data)))
		new = [x for x in prime if x != 0]
		#print(new)
		thouLen=(len(new))
		print(thouLen)
		#1 is added as prime, hence using 10002 instead of 10001
		if thouLen==10002:	
			print("here is the answer", max(new))
			#print(new)
			flag="false"
			break
		N=N+3 #increase N if the condition is not met
		
#time for execution of script
start_time = time.time()
thousandPrime()
print("--- %s seconds ---" % (time.time() - start_time))


