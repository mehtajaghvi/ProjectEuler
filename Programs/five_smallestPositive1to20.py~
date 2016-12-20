
################################
#Project Euler

#Problem Statement 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?.

################################
import time
import math

listL=[19,17,18,16,15,14,13,11]
#listL=[10,9,8,7]
maxNumber=20
infinite = int(math.factorial(maxNumber)/2)

def five_smallestNumber():
	flag='notDone'	
	theNumber=1
	for i in range (1,infinite+1):
		#for j in range (maxNumber,1,-1): #Generic
		for j in listL:			
			if i % j ==0:					    
			    if (j==listL[len(listL)-1]):
			    #if j==2: #Generic	
			    	flag='doneSearching'#To break the loop
			    	theNumber=i #This is the smallest number			    					
			else:			    			    
			    break

		if flag=='doneSearching':			
			break		
	print ("The number is", theNumber)			
	return theNumber

#time for execution of script
start_time = time.time()
five_smallestNumber()
print("--- %s seconds ---" % (time.time() - start_time))
