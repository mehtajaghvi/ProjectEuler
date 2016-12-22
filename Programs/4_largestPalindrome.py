
################################
#Project Euler

#Problem Statement 4

#Largest palindrome product
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


################################
import time
import math

def palinDrome(listPal):
	palCheck=[]
	#check if the reverse is same 
	for i in listPal:
		i=str(i)
		if i==i[::-1]:
			palCheck.append(i)
	return palCheck
	
#optimized palindrome	
def optPalindrome(x):
	y=0	
	x=str(x)
	if x==x[::-1]:
		y=x			
	else:
		y=0			
	return y		
	
def largePal():
	begin=100
	end=999
	listPal=[]
	for i in range(begin,end):		
		for j in range (begin,end):
			if (i%10==0):
				break
			elif (j%10==0):
				continue
			else:
				listPal.append(i*j)

	#Map each number to number itself or 0 (Palindrome or not Palindrome)
	#Filtering the Palindrome data
	palinDromes= list(map(optPalindrome, listPal))

	#converting string to integers
	palinDromes = [int(n) for n in palinDromes ]

	#Print the maximum palindrome from the entire list
	print(max(palinDromes))			
		

#time for execution of script
start_time = time.time()
largePal()
print("--- %s seconds ---" % (time.time() - start_time))


