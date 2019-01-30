#shanu
n,k=map(int,input().split())
m=list(map(int,input().split()))
c=0
for i in m:
    if i==k:
        c=c+1
if c>=1:
    print("Yes")
else:
    print("No")
