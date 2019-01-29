#shanu
n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(0,k):
    a.insert(0,a[-1])
    del(a[-1])
for j in range(len(a)):
    if c==0:
        print(a[j],end="")
        c=c+1
    else:
        print("",a[j],end="")

        
    
