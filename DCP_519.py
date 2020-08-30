def switch(x, y, b):
	return (x * b) | (y * (1 - b))

print(switch(9, 3, 1))
print(switch(9, 3, 0))
