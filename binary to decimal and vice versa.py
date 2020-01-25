'''
def btod(n):
    a=1
    s=0
    while n>0:
        rem=n%10
        s+=rem*a
        a*=2
        n=n//10
    return s
'''
'''
def dtob(n):
    a=1
    s=0
    while (n>0):
        rem=n%2
        s+=rem*a
        a*=10
        n=n//2
    return s
'''
