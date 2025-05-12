random_numbers = [1, 2, 3, 3, 4, 5, 6, 1, 7, 8, 9]

# Remove repetitions and sort the numbers
numbers = sorted(set(random_numbers), reverse=False)

for i in numbers:
    out = ""
    for j in range(i):
        out += "*"
    print(out.center(max(numbers)))

