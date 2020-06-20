a=input("type a number:")
b=input("b:")
a=int(a)
b=int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("b ! =0")
