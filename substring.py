#shanu
n,m=map(str,input().split())
if len(n)>=len(m):
    c=0
    for i in m:
        if i in n:
            c=c+1
    if c==len(m):
        print("yes")
    else:
        print("no")
else:
    print("no")
    
