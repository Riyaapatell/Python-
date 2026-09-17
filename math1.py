def func(a):
    fact = 1
    if a < 1:
        return False
    for i in range(1,a+1):
        fact = fact * i
    return fact
