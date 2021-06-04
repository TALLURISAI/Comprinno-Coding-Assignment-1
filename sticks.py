from sys import stdin, stdout 
def get_xs(Type=int): return map(Type, stdin.readline().strip().split())
def input_int(): return int(stdin.readline())
def write(w,end="\n"):stdout.write(str(w)+end)
for _ in range( input_int()):
    n=input_int()
    l=list(get_xs())
    l.sort(reverse=True)
    t=0
    c=0
    a=1
    for i in l:
        if i==t:
            a*=t
            t=0
            c+=1
            if c==2:
                write(a)
                break
        else:
            t=i
    else:
        write(-1)