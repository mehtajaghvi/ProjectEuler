
################################
#Project Euler

#Problem Statement 14
#Collatz

################################
import time
import math

			
lastlength=0
	
def collatz():
	#begin
	newlength=0
	lastlength=0	
	lastlength=newlength
	million=1000000
	#loop
	for n in range(3,million):
		number=n
		collatz=[]
		flag="nolog"
		#Based on the conjecture		
		while(n!=1):
			#for n even	
			if not(n%2):
				n=int(n/2)				
				logn=math.log(n,2)
				if logn.is_integer():
					newlength=len(collatz)+int(logn)+1+1
					flag="log"					
					break
				collatz.append(n)
			#for n odd				
			else:
				n=3*n+1
				logn=math.log(n,2)
				if logn.is_integer():
					newlength=len(collatz)+int(logn)+1+1
					flag="log"					
					break
				collatz.append(n)

		#+1 as number is not included in the list
		if flag=="nolog":
			newlength=len(collatz)+1
		
		if(newlength>lastlength):
			lastlength=newlength
			#numbe with the longest iterative series
			foundnumber=number
			#print("--- %d %d-%d--" , number, newlength) 
			#print (collatz)		
		
	return foundnumber
#time for execution of script
start_time = time.time()
result=collatz()
print(result)
print("--- %s seconds ---" % (time.time() - start_time))


