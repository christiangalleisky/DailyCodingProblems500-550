#checks if a input string is a palidrome
#or contains any palidromes

#junk attempt
#learned = at it's core, if it has more than 1 odd
#multiplicity of a letter it does not work
#
'''
def palindrome_checker(s):
		x = (len(s) // 2) - 1
		while x >= 0 : 
			if s[x] != s[len(s) - 1 - x]:
				print("Matched from center to index " + str(x+1))
				return False
			x -= 1
		return s
		
z = palindrome_checker("raceca")
print(z)
'''
'''
#good implementation
from collections import Counter

def is_permutation_palindrome(s):
    c = Counter(s)

    num_odds = 0 # Number of characters that have an odd count.

    for char, count in c.items():
        if count % 2 != 0:
            num_odds += 1

    return num_odds <= 1
'''   
'''    
#another good implementation
def is_permutation_palindrome_2ndImp(s):
    # There are 128 ASCII characters
    arr = [0 for _ in range(128)]

    num_odds = 0
    for char in s:
        i = ord(char)
        arr[i] += 1

        if arr[i] % 2 != 0:
            num_odds += 1
        else:
            num_odds -= 1

    return num_odds <= 1
'''
'''
arr = "SHARk"
for x in arr:
	print(x)
	i = ord(x)
	print(i)
'''
