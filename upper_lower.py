#shanu
n=input()
s=""
for i in n:
    if i.islower():
        s=s+i.upper()
    else:
        s=s+i.lower()
print(s)
    
