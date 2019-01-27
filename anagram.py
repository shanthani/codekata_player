#shanu
n=int(input())
s="kabali"
a=[]
c=0
d=0
for i in range(0,n):
      a.append(input())
print(a)
for t in range(0,len(s)):
      for j in range(0,len(a)):
            for k in range(0,len(a[j])):
                     if s.count(s[t])==a[j].count(a[j][k]):
                              c=c+1
      if c==len(s):
            d=d+1
print(d)
               
               
               
