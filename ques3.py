def evenProducer(n):
    a=2
    while n:
        yield a
        a+=2
        n-=1

num=int(input("Enter number :"))
# it=evenProducer(num)
for e in evenProducer(num):
    print(e,end=" ")