s="hello world"
result=''

for i in s:
    result+=chr(ord(i)+1)
#ord()是取得i的ASCII码

print(result)