import sys

input=sys.stdin.read

a=input()

print(a)

for i in range(len(a)):
    print(f"{i}:{a[i]}")

'''
3 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
'''
print(len(a))   # 输出 40
print(repr(a))  # 显示换行符