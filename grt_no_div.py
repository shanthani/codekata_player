#shanu
n,k=map(int,input().split())
s=min([n,k])
for i in range(1,s+1):
      if n%i==0 and k%i==0:
            e=i
print(e)
      
