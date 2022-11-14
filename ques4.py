def sqnum(n):
    a=1
    while n:
        yield a**2
        a+=1
        n-=1
    
num=int(input("Enter number :"))
for e in sqnum(num):
    print(e,end=" ")
    