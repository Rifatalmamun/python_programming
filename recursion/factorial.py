def factorial(n): 
    if(int(n)==n and n>0):
        if n in [0,1]:
            return 1;
        else:
            return n * factorial(n-1)

print(factorial(4.7)) 