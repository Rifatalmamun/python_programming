def digitSum(n):
    assert int(n)==n and n>=0, "Invalid"
    if n == 0:
        return 0 
    else:
        return int(n%10) + digitSum(int(n/10)) 

print(digitSum(12345)) 
        