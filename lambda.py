def myfunc1(n):
    return lambda a : a * n

def func2(n):
    return lambda b : n - b

mult = myfunc1(2)
print(mult(3))

subtract = func2(100)
print(subtract(51))