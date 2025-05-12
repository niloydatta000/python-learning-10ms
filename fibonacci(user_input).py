a, b = 0, 1 # initial variable declaration

n = int(input('How many numbers do you add in the sequence: ')) # user input

# Using for loop

for i in range(0,n):
	print(a)
	a, b = b, a + b