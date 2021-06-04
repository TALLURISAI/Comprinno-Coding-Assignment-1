#taking input size
for _ in range(int(input())):
    #taking sub inputs
    n=int(input())
    c=0
    d={0:0,1:0,-1:0}
    #taking sub array inputs
    for x in map(int,input().split()):
        if x not in d:
            c+=1
        else:
            d[x]+=1
        if c>1:
            print('no')
            break
    else:
        #checking the couple array and printing the result
        if c and d[-1]:
            print('no')
        elif d[-1]>1 and d[1]==0:
            print('no')
        else: 
            print('yes')