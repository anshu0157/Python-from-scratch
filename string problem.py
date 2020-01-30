'''st="what is your name"
b=""
for i in st:
    b=i+b
print(b)
'''
st=input("enter the string")
b=list(st)
p=0
for i in range(len(b)):
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
