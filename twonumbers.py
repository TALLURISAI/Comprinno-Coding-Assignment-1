try:
    t=int(input())
    while t>0:
        a,b,n=map(int,input().split())
        
        if n%2==0:
            print(max(a,b)//min(a,b))

        if n%2==1:
            a=a*2
            print(max(a,b)//min(a,b))
        
        t-=1
    
except:
    pass