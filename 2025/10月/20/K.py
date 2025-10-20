a=list(map(int,input().split()))

ans1=0
ans2=0

for i in range(0,len(a)):
    if a[i]>0:
        ans1+=1
    elif a[i]<0:
        ans2+=1

print(f"positive:{ans1}")
print(f"negative:{ans2}")