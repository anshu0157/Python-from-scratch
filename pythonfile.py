
def high(n):
    b=n%10
    temp=b
    while n>0:
        n=n//10
        d=n%10
        if temp>d:
            temp=temp
        else:
            temp=d
    return temp


def minm(n):
    b=n%10
    temp=b
    while n>0:
        n=n//10
        d=n%10
        if temp<d:
            temp=temp
        else:
            temp=d
    return temp


def prime(n):
    count=0
    while n>0:
        b=n%10
        n=n//10
        c=0
        for i in range(1,b+1):
            if b%i==0:
                c+=1
        if c==2:
            count+=1
            print(b,end=" ")
    print("\n","total prime no.",count)


def count_no(n):
    count=0
    while n>0:
        b=n%10
        count+=1
        n=n//10
    return count


def even(n):
    count=0
    while n>0:
        b=n%10
        n=n//10
        if b%2==0:
            print(b,end=" ")
            count+=1
    print("\n","total even no:",count)

def odd(n):
    count=0
    while n>0:
        b=n%10
        n=n//10
        if b%2!=0:
            print(b,end=" ")
            count+=1
    print("\n","total odd no:",count)


def sum_no(n):
    count=0
    s=0
    while n>0:
        b=n%10
        n=n//10
        s+=b
        count+=1
    return s
    print("total count of number:",count)


def reverse(n):
    while n>0:
        b=n%10
        n=n//10
        print(b,end=" ")
        
