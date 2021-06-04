#Taking input size and looping until the size is zero
for _ in range(int(input())):
    n = int(input())
    #checking the input is odd because the temple rto be constructed at center 
    if n%2 == 0:
        y = list(map(int,input().split()[:n]))
        print('no')
    else:
        #if odd take the inputs create the list l and print the result
        x = list(map(int,input().split()[:n]))
        l = []
        i = 0
        for j in range(n):
            if j > n/2 :
                i = i-1
                l.append(i)
            else:
                i = i+1
                l.append(i)
        if x==l:
            print('yes')
        else:
            print('no')
            