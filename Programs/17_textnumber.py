
################################
#Project Euler

#Problem Statement 17
#Number letter counts
################################
import time
import math
import itertools

def numtotext(number):
	
	unitlist=["null","one","two","three","four","five","six","seven","eight","nine"]
	tenslist=["null","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]			
	hundredlist=["null","onehundred","twohundred","threehundred","fourhundred","fivehundred","sixhundred","sevenhundred","eighthundred","ninehundred"]
	digit=[]	
	while number:
		digit.append(number%10)
		number=int(number/10)
	l=(len(digit))	
	
	if(l==3):
		if(digit[1]==1):							
			tn=digit[0]+1
			un=0	
			numtotext=[unitlist[un],tenslist[tn],hundredlist[digit[2]]]
		elif(digit[1]==0):
			tn=digit[1]
			numtotext=[unitlist[digit[0]],tenslist[tn],hundredlist[digit[2]]]
		else:
			tn=digit[1]+9
			numtotext=[unitlist[digit[0]],tenslist[tn],hundredlist[digit[2]]]
		if not(digit[1]==0) or not (digit[0]==0):
			numtotext.insert(2,"and")
		numtotext=numtotext[::-1]
	elif(l==2):
		if(digit[1]==1):
			#1 to skip ten							
			tn=digit[0]+1
			un=0	
			numtotext=[unitlist[un],tenslist[tn]]
		else:
			#9 to skip the nine strings in the list
			tn=digit[1]+9
			numtotext=[unitlist[digit[0]],tenslist[tn]]
		numtotext=numtotext[::-1]

	else:
		numtotext=[unitlist[digit[0]]]
	return (numtotext)

def text(n):
	l=[]
	for i in range(1,n):
		l.append(numtotext(i))
	#combine all the lists into one
	flattened_list  = list(itertools.chain(*l))
	#filter all the nulls
	refined_list = list(filter(lambda x: x!="null", flattened_list))
	return(refined_list)

#time for execution of script
start_time = time.time()	
result=text(1001)
result.append("onethousand")
sumalpha=0
for i in range(0,len(result)):
	sumalpha=sumalpha+len(result[i])	
print(sumalpha)
print("--- %s seconds ---" % (time.time() - start_time))


