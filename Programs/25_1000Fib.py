
################################
#Project Euler

#Problem Statement 25


################################
import time
import math
#some big number 
maxNumber=100000000

#max length of the 1000-digit number
maxLen=1000

def thou_FibNum():	
	secondLast=1
	last=2
	for n in range(1,maxNumber):
		next=secondLast+last 
		secondLast=last
		last=next		
		a=str(next)
		#print(a,len(a))
		if (len(a)>=maxLen):
			break
	indexFib=(n+3)		
	return indexFib

#time for execution of script
start_time = time.time()
result=thou_FibNum()
print(result)
print("--- %s seconds ---" % (time.time() - start_time))
