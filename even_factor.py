#shanu
def even(w):
    if w%2==0:
        return 1
    else:
        return 0

n=int(input())
count=0
for i in range(2,n+1):
    if n%i==0:
        if count==0:
            if even(i)==1:
                print(i,end="")
                count+=1
        else:
            if even(i)==1:
                print("",i,end="")
