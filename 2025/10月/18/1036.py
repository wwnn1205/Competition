a=list(map(int,input().split()))
a.sort()
print(f"{abs(int(a[0]+a[3]-a[1]-a[2]))}")