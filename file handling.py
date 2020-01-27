'''
data="my name is singh"
with open("singh.txt","wb") as f:
    a=f.write(data.encoe('utf-8'))
print(a)
'''
data=[]
s="brand\tcost\tqty\n"
def store():
    for i in data:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\n")
    
n=int(input("enter the value of n"))
for i in range(n):
            brand=input("enter the name of brand")
            cost=int(input("enter the price"))
            qty=int(input("enter the qty"))
            data.append([brand,cost,qty])
with open("product.txt","w") as f:
    f.write(s)
    for i in data:
        f.write(f"{i[0]}\t{i[1]}\t{i[2]}\n")
