a,b,c=map(int,input().split())

sm=a+b+c

ans=sm//3
if ans>=60:
    print("NO")
else:
    print("YES")