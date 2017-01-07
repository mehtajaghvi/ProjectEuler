
################################
#Project Euler

#Problem Statement 16
#Power digit sum

################################
import time
import math

			
	
def powersum():
	number=1000
	powersum=int(math.pow(2,number))	
	l2=[int(n) for n in str(powersum)] 
	powersum=sum(l2)
	return powersum

#time for execution of script
start_time = time.time()
result=powersum()

print(result)
print("--- %s seconds ---" % (time.time() - start_time))


