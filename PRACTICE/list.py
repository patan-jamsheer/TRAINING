# ==========================================
#        PYTHON LIST METHODS & OPERATIONS
# ==========================================

my_list = [1, 2, 3, 4, 5, 2]

print("Original List:", my_list)
print("=" * 50)


# ------------------------------------------------
# 1. append()
# Adds ONE element at the end
# ------------------------------------------------

my_list.append(6)

print("After append(6):")
print(my_list)
print()


# ------------------------------------------------
# 2. extend()
# Adds MULTIPLE elements
# ------------------------------------------------

my_list.extend([7, 8, 9])

print("After extend([7, 8, 9]):")
print(my_list)
print()


# ------------------------------------------------
# 3. insert()
# Adds an element at a specific index
# ------------------------------------------------

my_list.insert(3, 50)

print("After insert(3, 50):")
print(my_list)
print()


# ------------------------------------------------
# 4. remove()
# Removes the FIRST occurrence of a value
# ------------------------------------------------

my_list.remove(2)

print("After remove(2):")
print(my_list)
print()


# ------------------------------------------------
# 5. pop()
# Removes and returns an element
# Default: removes the last element
# ------------------------------------------------

removed_element = my_list.pop()

print("After pop():")
print(my_list)
print("Removed element:", removed_element)
print()


# ------------------------------------------------
# 6. pop(index)
# Removes element at a specific index
# ------------------------------------------------

removed_element = my_list.pop(2)

print("After pop(2):")
print(my_list)
print("Removed element:", removed_element)
print()


# ------------------------------------------------
# 7. count()
# Counts how many times a value occurs
# ------------------------------------------------

count = my_list.count(3)

print("Number of times 3 occurs:", count)
print()


# ------------------------------------------------
# 8. index()
# Returns the index of the FIRST occurrence
# ------------------------------------------------

index = my_list.index(5)

print("Index of 5:", index)
print()


# ------------------------------------------------
# 9. reverse()
# Reverses the list
# ------------------------------------------------

my_list.reverse()

print("After reverse():")
print(my_list)
print()


# ------------------------------------------------
# 10. sort()
# Sorts in ascending order
# ------------------------------------------------

my_list.sort()

print("After sort():")
print(my_list)
print()


# ------------------------------------------------
# 11. sort(reverse=True)
# Sorts in descending order
# ------------------------------------------------

my_list.sort(reverse=True)

print("After sort(reverse=True):")
print(my_list)
print()


# ------------------------------------------------
# 12. copy()
# Creates a copy of the list
# ------------------------------------------------

copied_list = my_list.copy()

print("Original List:")
print(my_list)

print("Copied List:")
print(copied_list)
print()


# ------------------------------------------------
# 13. clear()
# Removes all elements
# ------------------------------------------------

copied_list.clear()

print("After clear():")
print(copied_list)
print()


# ==========================================
#        COMMON LIST OPERATIONS
# ==========================================

numbers = [10, 20, 30, 40, 50]

print("=" * 50)
print("COMMON LIST OPERATIONS")
print("=" * 50)


# ------------------------------------------------
# 14. len()
# Returns number of elements
# ------------------------------------------------

print("Length:", len(numbers))
print()


# ------------------------------------------------
# 15. Indexing
# Access an element using its index
# ------------------------------------------------

print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Last element:", numbers[-1])
print()


# ------------------------------------------------
# 16. Slicing
# Extract a portion of the list
# ------------------------------------------------

print("numbers[1:4]:", numbers[1:4])
print("numbers[:3]:", numbers[:3])
print("numbers[2:]:", numbers[2:])
print("numbers[::-1]:", numbers[::-1])
print()


# ------------------------------------------------
# 17. in
# Checks whether an element exists
# ------------------------------------------------

print("30 in numbers:", 30 in numbers)
print()


# ------------------------------------------------
# 18. not in
# Checks whether an element doesn't exist
# ------------------------------------------------

print("100 not in numbers:", 100 not in numbers)
print()


# ------------------------------------------------
# 19. + operator
# Combines two lists
# ------------------------------------------------

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2

print("list1 + list2:")
print(combined_list)
print()


# ------------------------------------------------
# 20. * operator
# Repeats a list
# ------------------------------------------------

repeated_list = [1, 2] * 3

print("[1, 2] * 3:")
print(repeated_list)
print()


# ==========================================
#              FINAL SUMMARY
# ==========================================

print("=" * 50)
print("ALL IMPORTANT LIST METHODS")
print("=" * 50)

print("""
1.  append()       -> Add one element
2.  extend()       -> Add multiple elements
3.  insert()       -> Add at specific index
4.  remove()       -> Remove a specific value
5.  pop()          -> Remove and return element
6.  clear()        -> Remove all elements
7.  index()        -> Find index of a value
8.  count()        -> Count occurrences
9.  sort()         -> Sort the list
10. reverse()      -> Reverse the list
11. copy()         -> Create a copy
""")