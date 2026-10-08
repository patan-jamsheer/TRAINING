try:
    num=int(input("enter a number"))
    a=[1,2]
    print(a[num])
except ValueError:
    print("enter value is not an integer")
except IndexError:
    print("index error")