
################################
#Project Euler

#Problem Statement 6
#Sum square difference

#The sum of the squares of the first ten natural numbers is, 385
#The square of the sum of the first ten natural numbers is, 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
################################
import time
import math

def squares(s):
	return s*s			
	
def squareSum():
	N=101
	dataList=range(1,N)
	squared=map(squares, list(dataList))
	sumSquare=squares((sum(list(dataList))))		
	squareSum=(sum(list(squared)))
	print(sumSquare-squareSum)

#time for execution of script
start_time = time.time()
squareSum()
print("--- %s seconds ---" % (time.time() - start_time))


