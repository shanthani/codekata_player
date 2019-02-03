#shanu
n,k=map(str,input().split())
k=int(k)
a=list(n)
for i in range(0,k):
    a.insert(0,a[-1])
    del(a[-1])
print("".join(a))
