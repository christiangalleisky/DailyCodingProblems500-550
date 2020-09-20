import itertools as it

#chars = C, length = k, only
#works for k values less than or equal to 
#char array length
def DeBruijnSequence(C, k):
	x = it.permutations(C, k)
	return x
	
'''
To extend, add permutations groups to permutations elements
'''


s = "dad"
i = 3
x = DeBruijnSequence(s, i)
for chars in x:
	print(chars)
