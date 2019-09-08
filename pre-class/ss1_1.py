### cs110-ss1.1
### play with random module and while loop
#@jingren_wang

import random

# a function that sums num

def randSum():
	n = int(input("plesae enter the number of random numbers you want: "))
	randSum = 0	
	count = 0
	while count <= n:
		aNum = random.randrange(1,10)  #return an integer from 1 - 9
		randSum = randSum + aNum 
		count = count+1  #advance n by 1, otherwise an infinite loop

	return(randSum)


print(randSum())


