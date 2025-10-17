import sys
input=sys.stdin.read

a,b=map(int,input().split())

ans=a+b
if ans%7==0:
    print("7")
else:
    print(f"{ans%7}")