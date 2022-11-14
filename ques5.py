def fibonaci(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1
        
num=int(input("Enter number :"))
for e in fibonaci(num):
    print(e,end= " ")