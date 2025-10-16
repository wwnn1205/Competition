import sys
input = sys.stdin.read

a,b=map(int,input().split())

ans=b/a*100*1.0
print(f"{ans:.3f}%")