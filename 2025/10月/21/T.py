n,a,b=map(int,input().split())

ans=max(0,n-max(a+1,n-b)+1)

print(ans)