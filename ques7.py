def fibonacci(n):
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

n=int(input('Enter number :'))
for i in fibonacci(n):
    print(i,end=" ")      
