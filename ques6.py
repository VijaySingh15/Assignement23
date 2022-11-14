def isPrime(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

def primeNum(n):
    a=2
    while n:
        if isPrime(a):
            yield a
            n-=1
        a+=1
    return

number=int(input("Enter number :"))
it=primeNum(number)
for e in it:
    print(e,end=" ")
         