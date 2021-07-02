def solution(n):
    lst = []
    lst = list(map(int, input().split()[:n]))

    for i in lst:
            flag = 0
            for j in range(2,i,1):
                if(i%j==0):
                    flag = flag + 1
            if(flag==1):
                print("YES")
            else:
                print("NO")
    
# main function 
if __name__=='__main__':
    n = int(input())
    solution(n)