def oddProducer(n):
    a=1
    while n:
        yield a
        a+=2
        n-=1
        
num=int(input("Enter number :"))
for e in oddProducer(num):
    print(e,end=" ")