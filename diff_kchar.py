#shanu
n,k,m=map(str,input().split())
c=0
m=int(m)
for i in range(len(n)):
    for j in range(len(k)):
        if i==j:
            if n[i]!=k[j]:
                c=c+1
if c==m:
    print("yes")
else:
    print("no")
