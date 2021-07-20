def fibonacci(n):
    assert int(n)==n and n>=0, "Fibonacci number can not be negative or non intiger"
    if n in [0,1]:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2) 

print(fibonacci(4))
        