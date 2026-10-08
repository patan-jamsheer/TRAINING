# ==========================================
#        PYTHON STRING METHODS
# ==========================================

text = "  Hello Python World  "

print("Original String:", repr(text))
print("=" * 60)


# =========================================================
# 1. upper()
# Converts all letters to uppercase
# =========================================================

print("upper():", text.upper())


# =========================================================
# 2. lower()
# Converts all letters to lowercase
# =========================================================

print("lower():", text.lower())


# =========================================================
# 3. capitalize()
# First character becomes uppercase
# =========================================================

print("capitalize():", text.capitalize())


# =========================================================
# 4. title()
# First letter of every word becomes uppercase
# =========================================================

print("title():", text.title())


# =========================================================
# 5. swapcase()
# Uppercase -> lowercase
# Lowercase -> uppercase
# =========================================================

print("swapcase():", text.swapcase())


# =========================================================
# 6. casefold()
# Similar to lower(), but stronger for comparisons
# =========================================================

print("casefold():", text.casefold())


# =========================================================
# 7. strip()
# Removes spaces from beginning and end
# =========================================================

print("strip():", text.strip())


# =========================================================
# 8. lstrip()
# Removes spaces from the left
# =========================================================

print("lstrip():", text.lstrip())


# =========================================================
# 9. rstrip()
# Removes spaces from the right
# =========================================================

print("rstrip():", text.rstrip())


# =========================================================
# 10. replace()
# Replaces one substring with another
# =========================================================

sentence = "I love Java"

print("replace():", sentence.replace("Java", "Python"))


# =========================================================
# 11. split()
# Converts string into a list
# =========================================================

sentence = "Python is very easy"

print("split():", sentence.split())


# =========================================================
# 12. split(separator)
# Splits using a specific separator
# =========================================================

data = "apple,banana,mango,orange"

print("split(','):", data.split(","))


# =========================================================
# 13. rsplit()
# Splits from the right
# =========================================================

data = "one-two-three-four"

print("rsplit('-', 1):", data.rsplit("-", 1))


# =========================================================
# 14. splitlines()
# Splits a multiline string into lines
# =========================================================

data = """Python
Java
C++
JavaScript"""

print("splitlines():", data.splitlines())


# =========================================================
# 15. join()
# Joins elements into one string
# =========================================================

words = ["Python", "is", "easy"]

print("join():", " ".join(words))


# =========================================================
# 16. find()
# Returns index of first occurrence
# Returns -1 if not found
# =========================================================

text = "Hello Python"

print("find('Python'):", text.find("Python"))
print("find('Java'):", text.find("Java"))


# =========================================================
# 17. rfind()
# Finds from the right
# =========================================================

text = "Python is easy and Python is powerful"

print("rfind('Python'):", text.rfind("Python"))


# =========================================================
# 18. index()
# Similar to find()
# BUT raises an error if not found
# =========================================================

text = "Hello Python"

print("index('Python'):", text.index("Python"))


# =========================================================
# 19. rindex()
# Finds last occurrence
# Raises error if not found
# =========================================================

text = "Python is easy and Python is powerful"

print("rindex('Python'):", text.rindex("Python"))


# =========================================================
# 20. count()
# Counts occurrences
# =========================================================

text = "banana"

print("count('a'):", text.count("a"))


# =========================================================
# 21. startswith()
# Checks beginning of string
# =========================================================

text = "Python Programming"

print("startswith('Python'):", text.startswith("Python"))


# =========================================================
# 22. endswith()
# Checks ending of string
# =========================================================

print("endswith('Programming'):", text.endswith("Programming"))


# =========================================================
# 23. isalpha()
# Checks whether ALL characters are alphabets
# =========================================================

print("'Python'.isalpha():", "Python".isalpha())
print("'Python123'.isalpha():", "Python123".isalpha())


# =========================================================
# 24. isdigit()
# Checks whether ALL characters are digits
# =========================================================

print("'12345'.isdigit():", "12345".isdigit())
print("'123abc'.isdigit():", "123abc".isdigit())


# =========================================================
# 25. isalnum()
# Checks whether characters are alphabets OR numbers
# =========================================================

print("'Python123'.isalnum():", "Python123".isalnum())
print("'Python 123'.isalnum():", "Python 123".isalnum())


# =========================================================
# 26. isspace()
# Checks whether all characters are whitespace
# =========================================================

print("'   '.isspace():", "   ".isspace())
print("'Python'.isspace():", "Python".isspace())


# =========================================================
# 27. islower()
# Checks whether all cased characters are lowercase
# =========================================================

print("'hello'.islower():", "hello".islower())


# =========================================================
# 28. isupper()
# Checks whether all cased characters are uppercase
# =========================================================

print("'HELLO'.isupper():", "HELLO".isupper())


# =========================================================
# 29. istitle()
# Checks whether string follows title-case format
# =========================================================

print("'Hello World'.istitle():", "Hello World".istitle())


# =========================================================
# 30. isdecimal()
# Checks decimal characters
# =========================================================

print("'123'.isdecimal():", "123".isdecimal())


# =========================================================
# 31. isnumeric()
# Checks whether characters are numeric
# =========================================================

print("'123'.isnumeric():", "123".isnumeric())


# =========================================================
# 32. isidentifier()
# Checks whether string can be a valid Python identifier
# =========================================================

print("'variable'.isidentifier():", "variable".isidentifier())
print("'123variable'.isidentifier():", "123variable".isidentifier())


# =========================================================
# 33. isprintable()
# Checks whether all characters are printable
# =========================================================

print("'Hello'.isprintable():", "Hello".isprintable())


# =========================================================
# 34. isascii()
# Checks whether all characters are ASCII
# =========================================================

print("'Hello'.isascii():", "Hello".isascii())


# =========================================================
# 35. zfill()
# Adds zeros to the LEFT
# =========================================================

number = "42"

print("zfill(5):", number.zfill(5))


# =========================================================
# 36. center()
# Centers the string
# =========================================================

print("center():", "Python".center(20, "-"))


# =========================================================
# 37. ljust()
# Left-aligns the string
# =========================================================

print("ljust():", "Python".ljust(15, "-"))


# =========================================================
# 38. rjust()
# Right-aligns the string
# =========================================================

print("rjust():", "Python".rjust(15, "-"))


# =========================================================
# 39. removeprefix()
# Removes prefix if present
# =========================================================

text = "HelloPython"

print("removeprefix():", text.removeprefix("Hello"))


# =========================================================
# 40. removesuffix()
# Removes suffix if present
# =========================================================

text = "PythonWorld"

print("removesuffix():", text.removesuffix("World"))


# =========================================================
# 41. partition()
# Splits into THREE parts
# =========================================================

text = "Python-is-easy"

print("partition():", text.partition("-"))


# =========================================================
# 42. rpartition()
# Partition from the RIGHT
# =========================================================

text = "Python-is-very-easy"

print("rpartition():", text.rpartition("-"))


# =========================================================
# 43. translate()
# Replaces characters according to a translation table
# =========================================================

table = str.maketrans("aeiou", "12345")

text = "hello"

print("translate():", text.translate(table))


# =========================================================
# 44. expandtabs()
# Replaces tab characters with spaces
# =========================================================

text = "Python\tProgramming"

print("expandtabs():", text.expandtabs(4))


# =========================================================
# 45. encode()
# Converts string into bytes
# =========================================================

text = "Hello"

print("encode():", text.encode())


# =========================================================
# 46. format()
# Inserts values into a string
# =========================================================

name = "Chandu"
age = 20

print("format():", "My name is {} and I am {} years old".format(name, age))


# =========================================================
# 47. format_map()
# Uses a dictionary for formatting
# =========================================================

data = {
    "name": "Chandu",
    "age": 20
}

print(
    "format_map():",
    "My name is {name} and I am {age} years old".format_map(data)
)


# =========================================================
# 48. casefold() comparison example
# =========================================================

a = "PYTHON"
b = "python"

print("Case-insensitive comparison:", a.casefold() == b.casefold())


# =========================================================
#                STRING SUMMARY
# =========================================================

print("=" * 60)
print("IMPORTANT STRING METHODS")
print("=" * 60)

print("""
upper()
lower()
capitalize()
title()
swapcase()
casefold()

strip()
lstrip()
rstrip()

replace()

split()
rsplit()
splitlines()
join()

find()
rfind()
index()
rindex()
count()

startswith()
endswith()

isalpha()
isdigit()
isalnum()
isspace()
islower()
isupper()
istitle()
isdecimal()
isnumeric()
isidentifier()
isprintable()
isascii()

zfill()
center()
ljust()
rjust()

removeprefix()
removesuffix()

partition()
rpartition()

translate()
expandtabs()
encode()

format()
format_map()
""")