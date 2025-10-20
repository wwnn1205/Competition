l=[]
for i in range(0,3):
    l.append(int(input()))

l.sort()

if l[0]==l[1]==l[2]==1:
    print(3)
elif l[0]==1:
    print((l[0]))
