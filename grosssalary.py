a=int(input())
for i in range(a):
    n=int(input())
    if n<1500:
        print(2*n)
    else:
        print(n+500+0.98*n)