import math

a,b,c=map(int,input().split())
s=(a+b+c)/2
ans=s*(s-a)*(s-b)*(s-c)
ans=math.sqrt(ans)
print(f"circumference={a+b+c:.2f} area={ans:.2f}")