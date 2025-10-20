a=int(input())
ans=a*12*2.54*10
if ans*10%10==0:
    print(f"{ans:.0f}")
else:
    print(f"{ans}")