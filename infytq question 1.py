if __name__=="__main__":
    
    a = input('enter the value').split(',')
    b=list("".join(a))
    num1=0
    num2=''
    i=0
    n=len(b)
    while i<n:
        if a[i]=='5':
            while a[i]!='8':
                num2+=a[i]
                i+=1
            num2+=a[i]
        else:
            num1+=int(a[i])
        i+=1
    print(num1,num2)
    print(num1+int(num2))
