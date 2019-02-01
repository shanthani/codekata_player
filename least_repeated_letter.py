#shan
n=input()
a=[]
d={}
for i in n:
    if i==" ":
        pass
    else:
        s=n.count(i)
        d.update({i:s})
        a.append(s)
w=min(a)
c=0
for x,y in d.items():
     if y==w:
        if c==0:
            print(x,end="")
            c=c+1
        else:
            print("",x,end="")
