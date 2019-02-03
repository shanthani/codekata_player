#shanu
n=int(input())
k=list(map(int,input().split()))
s=sorted(k)
c=0
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            if k[i]==s[j]:
                c=c+1
if c==n:
    print("yes")
else:
    print("no")


