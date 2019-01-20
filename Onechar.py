s,r=map(str,input().split())
c=0
for i in range(0,len(s)):
    for j in range(0,len(r)):
        if i==j:
            if s[i]!=r[j]:
                c+=1
if c==1:
    print("yes")
else:
    print("no")
    
