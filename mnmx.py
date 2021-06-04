for _ in range(int(input())):
    n=int(input())
    l=[int(n) for n in input().split()]
    t=min(l)
    print(t*(n-1))