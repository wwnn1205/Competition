import math

a,b,c=map(int.input().split())

v=math.sqrt(a*b*c)

x=v//a
y=v//b
z=v//c

print(f"{4*(x+y+z)}")