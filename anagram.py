#shanu
n=int(input())
s="kabali"
a=[]
d=0
for i in range(0,n):
      a.append(input())
for j in a:
    c=0
    for k in j:
        if k in s:
            if s.count(k)==j.count(k):
                c=c+1
    if c==len(s):
        d=d+1
print(d)
