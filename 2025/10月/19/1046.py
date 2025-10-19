a,b,c=map(int,input().split())

ans1=min(b,c)
ans2=0;
sm=b+c
if sm>a:
    ans2=sm-a
print(f"{ans1} {ans2}")