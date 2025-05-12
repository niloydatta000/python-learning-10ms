# Fibonacci Sequence

fibo1 = 0
fibo2 = 1

# A somewhat TRICKY method is going to be applied

for i in range(10):
    print(fibo1)
    temp = fibo2 # A temporary variable is introduced to avoid interference
    fibo2 = fibo1 + fibo2
    # Now safely transfer fibo2 data into fibo1
    fibo1 = temp