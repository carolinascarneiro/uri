# even.py

# Make a program that reads five integer values. 
# Count how many of these values ​​are even and  print this information like the following example.

# Input
# The input will be 5 integer values.

# Output
# Print a message like the following example with all letters in lowercase,
#  indicating how many even numbers were typed.

def even(a, b, c, d, e):
    ns = [a, b, c, d, e]
    even = []
    for i in ns:
        if i % 2 == 0:
            even.append(i)
    print(len(even), "valores pares")

even(2, 4, 6, 8, 10)
