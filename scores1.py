# def scores(a, b):
#     return [a, b]
print("Write your first grade here:")
grade1 = list(float(input()))
print("Now write your second grade here:")
grade2 = list(float(input()))
scores = grade1 + grade2
print(scores)
for i in scores:
    print("Your grade is invalid") if i < 0 or i > 10 else print((a+b)/2)