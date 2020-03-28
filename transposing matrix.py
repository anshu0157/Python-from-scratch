#Transposing of matrix
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
s=[]
for i in range(4):
    d=[]
    for j in matrix:
        d.append(j[i])
    s.append(d)
    
print(s)
#Nested list comprehension(transposing of matrix)
a=[[row[p] for row in matrix] for p in range(4)]
print(a)
#Creating of matrix
m1=[]
for i in range(4):
    m2=[]
    for j in range(3):
        m2.append(3*i+j)
    m1.append(m2)
print(m1)
#creating matrix by list comprehension
matt=[[3*i+j for j in range(3)] for i in range(4)]
print(matt)
