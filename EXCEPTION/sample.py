try:
    print("hello world" + 5)
except TypeError:
    print("type error bro")


# | Exception           | When it happens                           | Example            |
# | ------------------- | ----------------------------------------- | ------------------ |
# | `ValueError`        | Wrong type of value                       | `int("abc")`       |
# | `TypeError`         | Incompatible types/operation              | `"10" + 5`         |
# | `IndexError`        | Invalid list/string index                 | `a[10]`            |
# | `KeyError`          | Dictionary key doesn't exist              | `d["xyz"]`         |
# | `ZeroDivisionError` | Division by zero                          | `10 / 0`           |
# | `NameError`         | Variable doesn't exist                    | `print(x)`         |
# | `AttributeError`    | Object doesn't have that attribute/method | `"hello".append()` |
# | `FileNotFoundError` | File doesn't exist                        | `open("abc.txt")`  |
