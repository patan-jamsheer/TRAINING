# ==========================================
#          PYTHON TUPLES
# ==========================================

numbers = (10, 20, 30, 20, 40, 20)

print("Original tuple:", numbers)


# 1. Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])


# 2. Slicing
print("Slicing:", numbers[1:4])


# 3. Length
print("Length:", len(numbers))


# 4. count()
print("Count of 20:", numbers.count(20))


# 5. index()
print("First index of 20:", numbers.index(20))


# 6. Membership
print("30 in tuple:", 30 in numbers)
print("100 in tuple:", 100 in numbers)


# 7. Tuple concatenation
a = (1, 2, 3)
b = (4, 5, 6)

print("Concatenation:", a + b)


# 8. Tuple repetition
print("Repetition:", (1, 2) * 3)


# 9. Tuple unpacking
student = ("Chandu", 20, "AIML")

name, age, branch = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)


# 10. Swapping
x = 10
y = 20

x, y = y, x

print("x:", x)
print("y:", y)


# 11. Tuple -> List
numbers_list = list(numbers)

print("Tuple to list:", numbers_list)


# 12. List -> Tuple
new_tuple = tuple(numbers_list)

print("List to tuple:", new_tuple)


# 13. Built-in functions
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))