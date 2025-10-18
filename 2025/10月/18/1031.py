a=int(input())

h=a//3600
if h!=0:
    a-=3600*h

m=a//60
if m!=0:
    a-=60*m

print(f"{h} {m} {a}")