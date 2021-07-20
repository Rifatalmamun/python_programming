def sum(n):
    assert int(n)==n and n>=0, "Invalid"
    if n == 1:
        return n 
    else:
        return sum(n-1)+n

print(sum(100))
        