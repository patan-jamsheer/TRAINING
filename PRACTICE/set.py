# ==========================================
#              PYTHON SETS
# ==========================================

# 1. Creating a Set
numbers = {1, 2, 3, 4, 5}
print("Set:", numbers)


# 2. Empty Set
empty_set = set()
print("Empty set:", empty_set)


# 3. Duplicate Values
numbers = {1, 2, 2, 3, 3, 4}
print("Duplicates removed:", numbers)


# 4. add()
numbers.add(10)
print("After add(10):", numbers)


# 5. update()
numbers.update([20, 30, 40])
print("After update():", numbers)


# 6. remove()
numbers.remove(10)
print("After remove(10):", numbers)


# 7. discard()
numbers.discard(100)   # No error if element doesn't exist
print("After discard(100):", numbers)


# 8. pop()
removed = numbers.pop()
print("After pop():", numbers)
print("Removed element:", removed)


# 9. clear()
temp = {1, 2, 3}
temp.clear()
print("After clear():", temp)


# ==========================================
#          SET OPERATIONS
# ==========================================

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 10. Union
print("Union:", A | B)
print("Union using method:", A.union(B))


# 11. Intersection
print("Intersection:", A & B)
print("Intersection using method:", A.intersection(B))


# 12. Difference
print("A - B:", A - B)
print("A difference B:", A.difference(B))

print("B - A:", B - A)


# 13. Symmetric Difference
print("Symmetric Difference:", A ^ B)
print("Using method:", A.symmetric_difference(B))


# ==========================================
#          SET RELATIONSHIPS
# ==========================================

X = {1, 2, 3}
Y = {1, 2, 3, 4, 5}
Z = {10, 20, 30}

# 14. issubset()
print("X subset of Y:", X.issubset(Y))


# 15. issuperset()
print("Y superset of X:", Y.issuperset(X))


# 16. isdisjoint()
print("X and Z are disjoint:", X.isdisjoint(Z))


# ==========================================
#          MEMBERSHIP
# ==========================================

numbers = {10, 20, 30, 40}

# 17. in
print("20 in set:", 20 in numbers)

# 18. not in
print("50 not in set:", 50 not in numbers)


# ==========================================
#          SET UPDATE METHODS
# ==========================================

A = {1, 2, 3}
B = {3, 4, 5}

# 19. update()
A.update(B)
print("After update:", A)


# 20. intersection_update()
A = {1, 2, 3}
B = {2, 3, 4}

A.intersection_update(B)
print("After intersection_update:", A)


# 21. difference_update()
A = {1, 2, 3}
B = {2, 3, 4}

A.difference_update(B)
print("After difference_update:", A)


# 22. symmetric_difference_update()
A = {1, 2, 3}
B = {3, 4, 5}

A.symmetric_difference_update(B)
print("After symmetric_difference_update:", A)


# ==========================================
#          COPY
# ==========================================

A = {1, 2, 3}

B = A.copy()

print("Original:", A)
print("Copy:", B)


# ==========================================
#          CONVERSION
# ==========================================

# List -> Set
numbers_list = [1, 2, 2, 3, 3, 4]

numbers_set = set(numbers_list)

print("List:", numbers_list)
print("Set:", numbers_set)


# Set -> List
new_list = list(numbers_set)

print("Set to list:", new_list)


# ==========================================
#          BUILT-IN FUNCTIONS
# ==========================================

numbers = {10, 20, 30, 40, 50}

print("Length:", len(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))


# ==========================================
#          FROZENSET
# ==========================================

numbers = frozenset([1, 2, 3, 4])

print("Frozenset:", numbers)

# numbers.add(5)  # Error: frozenset cannot be modified