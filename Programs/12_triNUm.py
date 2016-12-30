
################################
#Project Euler

#Problem Statement 12


################################
import time
import math
import sys

#using yield
def divisible(n):
	tri=n*(n+1)
	tri=int(tri/2)
	large_divisors = []
	for i in range(1,int(math.sqrt(tri))+1):
        	if tri % i == 0:
        		yield i
			#print(list(large_divisors)) 
        		if i*i != tri:
                    		large_divisors.append(tri / i)
	#print(list(reversed(large_divisors)))
	for divisor in reversed(large_divisors):
        	yield divisor
	
	return (large_divisors)		

#using no yield
def divisible_unoptimized(n):
	tri=int(n*(n+1))/2
	div=0
	number=0
	for i in range(1,int(math.sqrt(tri))+1):
		if(tri%i==0):
			div=div+2
	if div>500:
		number=tri		
	return number

#time for execution of script
start_time = time.time()
numberMin=12000

#magic number, found using intution
numberMax=12375
number=numberMax

#loop thru to find the magic number
#for i in range(numberMax,1,-1):
optimized=0
if optimized==1:
	result=list(divisible(numberMax))
	if len(result)>500:		
		print(len(result))
		print(result[-1])
		#print(result)
else:
	result=(divisible_unoptimized(numberMax))
	print(result)
	
	
print("--- %s seconds ---" % (time.time() - start_time))
