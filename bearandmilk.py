#Accepting the size
for _ in range(int(input())):
    #accepting the list size
    n=int(input())
    #accing the string list i.e cookie or milk
    a=list(input().split())
    c=0
    #checking if the bear drinks milk after cookie or not
    for i in a:
        if i=="cookie":
            c+=1 
        else:
            c=0
        if c==2:
            break
    #printing the result
    if c!=0:
        print("NO")
    else:
        print("YES")
