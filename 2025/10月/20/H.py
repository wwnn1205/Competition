a,b,c=map(int,input().split())

sm=a+b

if sm>c:
    print("NO")
else:
    cha=c-sm
    if cha%2==0:
        print("YES")
    else:
        print("NO")