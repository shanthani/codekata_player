n=int(input())
s=input()
vowels=["a","e","i","o","u"]
w=""
for i in s:
    if i not in vowels:
        w=w+i
print(w[::-1])
        
