def decor_coprime(hcf_func):
    def coprime(num1,num2):
        if num1>num2:
            min1=num2
        else:
            min1=num1
        for i in range(1,min1+1):
            if ((num1%i==0)and(num2%i==0)):
                h=i
        if h==1:
            print("Co-prime")
        hcf_func(num1,num2)
    return coprime

@decor_coprime
def hcf(num1,num2):
    if num1>num2:
        min1=num2
    else:
        min1=num1
    for i in range(1,min1+1):
        if ((num1%i==0)and(num2%i==0)):
            h=i
    else:
        print("HCF is :",h)

num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
hcf(num1,num2)