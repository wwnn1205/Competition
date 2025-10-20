a=input()

ans=a[-2:]
m=int(ans)

if m>=3 and m<=5:
    print("spring")
elif m>=6 and m<=8:
    print("summer")
elif m>=9 and m<=11:
    print("autumn")
else:
    print("winter")