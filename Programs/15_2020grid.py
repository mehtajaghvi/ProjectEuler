
################################
#Project Euler

#Problem Statement 15
#2020grid

################################
import time
import math

			
	

def grid():
	row=20
	column=20
	totalsteps=row+column
	right=column
	down=row
	total=math.factorial(totalsteps)
	right=math.factorial(column)
	down=math.factorial(row)
	result=int(total/(right*down))
	print(result)			
	

#time for execution of script
start_time = time.time()
grid()
print("--- %s seconds ---" % (time.time() - start_time))


