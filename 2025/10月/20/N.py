a=int(input())
b=int(input())
c=int(input())

ans1=a+b*c
ans2=a*(b+c)
ans3=a*b*c
ans4=(a+b)*c
ans5=a+b+c
ans6=a*b+c

print(max(ans1,ans2,ans3,ans4,ans5,ans6))