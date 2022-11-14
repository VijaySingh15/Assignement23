def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
        
def primeNum(n):
    a=2
    while True:
        if isPrime(a):
            yield a
        a+=1

num=int(input("Enter any number for endless Prime number :"))
for e in primeNum(num):
    print(e,end=" ")
