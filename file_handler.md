# Data manipulation on current directory: Data reading, data writing, data appending

Open a file using python script

```python
# 1. read data


f = open('data.txt', 'r') # Here f is not a list but object.
'''
full directory is required in parameter 1 but not necessary in the same directory.
Parameter 2 gets mode as command. Here 'r' stands for read text.
'''
print(f.read())

'''
To read parts from the file put an integer parameter in read() method.
For example, f.read(10) will read 10 characters for calling each time.
'''

for line in f:
	print(line) # This for loop will read every line.


# lines = f.readlines()
# print(lines) # List as lines[] will be applicable here.

f.close() # This close() must be written to close operations.
```

Create a file using python code

```python
# 2. write data

f = open('data.txt', 'w') # Here 'w' stands for write text.
f.write("Input text")

'''
This 'w' will over-write or reset data into "Input text".
All previous data will be deleted.
'''

f.close() # This close() must be written to close operations.
```

Append content

```python
# 3. append data

f = open('data.txt', 'a') # Here 'a' stands for append text.
f.write("\nInput text")

'''
This 'a' will append "Input text" after existing data in new line.
All previous data remain intact.
'''

f.close() # This close() must be written to close operations.
```

## Context Manager:


Applying Context Manager, There is no need for close() operation.
After moving out from with loop automatically it will be done.

```python
# 1. read data


with open('data.txt', 'r') as f:
	print(f.read())

	'''
	To read parts from the file put an integer parameter inside the parenthesis.
	For example, f.read(10) will read 10 characters for calling each time.
	'''

	for line in f:
		print(line) # This for loop will read every line.


	# lines = f.readlines()
	# print(lines) # List as lines[] will be applicable here.




# 2. write data

with open('data.txt', 'w') as f:
	f.write("Input text")

	'''
	This 'w' will over-write or reset data into "Input text".
	All previous data will be deleted.
	'''



# 3. append data

with open('data.txt', 'a') as f:
	f.write("\nInput text")
	
	'''
	This 'a' will append "Input text" after existing data in new line.
	All previous data will remain intact.
	'''
```
