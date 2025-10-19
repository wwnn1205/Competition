import math

a=int(input())

if a==1 or a==2:
    print(0)
else:
    a-=2
    ans=math.ceil(a/2)
    print(ans)