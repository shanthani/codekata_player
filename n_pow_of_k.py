#shanu
n,k=map(int,input().split())
for i in range(1,n):
    if k**i==n:
        print("yes")
        break
else:
    print("no")
    
