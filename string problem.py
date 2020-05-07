st=input("enter the string")
b=list(st)
c=len(b)
p=0
for i in range(c):
    if st[i+1]==" ":
        x=st[i]
        y=p
        while x<y:
            temp=x
            x=y
            y=temp
            x=x+1
            y+=1
    p=i+2
b=""
for i in st:
    b=i+b
print(b)
