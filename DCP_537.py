import random

#every number treated in this fashion
#converges to 1
def Collatz_sequence(num):
	
	occurances = 0
	while num > 1:
		if 0 == num % 2:
			num = num // 2
			occurances += 1
		else:
			num = (3*num) + 1
			occurances += 1
	return num, occurances

#driver
x = 1000000
maxOccurances = 0
while x > 0:
	n = random.randint(2, 1000000)
	num_one, occurances = Collatz_sequence(n)
	print(num_one)
	maxOccurances = max(occurances, maxOccurances)
	x -= 1
print(maxOccurances)
