#shanu
def isprime(w):
    c=0
    for j in range(2,w):
        if w%j==0:
            c=c+1
    if c==0:
        return 1
    else:
        return 0

n=int(input())
count=0
for i in range(2,n+1):
    if n%i==0:
        if count==0:
            if isprime(i)==1:
                print(i,end="")
                count+=1
        else:
            if isprime(i)==1:
                print("",i,end="")

