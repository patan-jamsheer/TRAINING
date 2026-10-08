try:
    a = 10
    b = 10
    print(a / b)
    with open("sample.txt","r") as f:
        f.read()

except ZeroDivisionError:
    print("You cannot divide by zero")
except IndexError:
    print("Index Error")
except ValueError:
    print("invalid input")
except FileNotFoundError:
    print("file not found")
finally:
    print("program finished")