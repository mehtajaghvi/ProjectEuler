
################################
#Project Euler

#Problem Statement n

################################
import time
import math
from functools import reduce 
#a+b>c and a+b+c=1000 ==>c<=500 ==>a <=250  250<b<=500
		
def sum_abc(listNum):
	#sum of all the numbers in the list
	result=reduce(lambda x, y: x+y, listNum)
	return result

def prod_abc(listNum):
	#product of all the numbers in the list
	result=reduce(lambda x, y: x*y, listNum)
	return result
		
def pyTri():
	nSum=1000
	abcList=[]
	
	la=list(range(1,int(nSum/4)))
	lb=list(range(int(nSum/4),int(nSum/2)))
	lc=list(range(1,int(nSum/2)))
	#for (c,b,a) in [(c,b,a) for c in (lc) for b in (lab) if b<c for a in (lab) if a<b and (a*a+b*b==c*c)]:
	#	abcList.append([a,b,c])

	for c in lc:
		for b in lb:
			for a in la: 
				if (a<b and a*a+b*b==c*c):
					abcList.append([a,b,c])

	#find sum of all the pythogoras a,b,c
	triSum=list(map(sum_abc,abcList))
	
	#find the index of [a,b,c] whose sum is 1000
	listOne=[i for i,x in enumerate(triSum) if x==1000]
	
	#sum of a,b,c 	
	abc=((abcList[listOne[0]]))	
	result=prod_abc(abc)
	return result

#time for execution of script
start_time = time.time()
result=pyTri()
print (result)
print("--- %s seconds ---" % (time.time() - start_time))


