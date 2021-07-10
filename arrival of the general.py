def max_position(lst):
    max = lst[0]
    
    for i in range(len(lst)):
        if(lst[i]>max):
            max = lst[i]
    return max 


def min_position(lst):
    min = lst[0]

    for i in range(len(lst)):
        if(lst[i]<min):
            min = lst[i]
    return min


if __name__=="__main__":
    n = int(input())
    
    lst=[]
    
    for i in range(1,n+1,1):
        inp = int(input())
        lst.append(inp)
        
    mx_position = max_position(lst)
    mn_positino = min_position(lst)
    
    print('-----------')
    
    print(mx_position)
    print(mn_positino)
    
    #print(find_solution(lst,max_value,min_value))




