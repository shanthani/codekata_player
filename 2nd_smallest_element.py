#shanu
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i!=min(a):
        b.append(i)
print(min(b))
