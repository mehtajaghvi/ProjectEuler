
################################
#Project Euler

#Problem Statement 18
#Power digit sum

################################
import time
import math


def triangle():
	mainL=[3],[7, 4],[2, 4, 6],[8, 5, 9, 3]
	mainL=[[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]
	summ=0
	maxsum=mainL[0][0]
	idx=0
	for i in range(0,len(mainL)-1):
		#main list
		#print("list",l1[i])	
		#short list with the adjacent numbers	
		l=mainL[i+1][idx:idx+2]		
		print("shortlist",l)		
		#max in the shortlist
		idxmaxshort=(l.index(max(l)))
		print(max(l))		
		summ=(max(l))
		maxsum=summ+maxsum
		#find the index of the max number in the short list in the original list of which shortlist is subset		
		idxMax=[i for i,x in enumerate(mainL[i+1]) if x == l[idxmaxshort]]
		#set that as the index for next short list	
		number=[i for i,x in enumerate(idxMax) if x==idx or x==idx+1]
		idx=idxMax[number[0]]	
		print(idx)
	return maxsum
#time for execution of script
start_time = time.time()
result=triangle()
print(result)
print("--- %s seconds ---" % (time.time() - start_time))


