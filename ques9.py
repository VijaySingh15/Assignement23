def decor_triangle(perimeter_func):
    def validity(l,b,h):
        if l==b==h:
            print("Equilateral Triangle")
        elif l==b!=h or l!=b==h or l==h!=b:
            print("Isoceles Triangle")
        else:
            print("Scalene Triangle")
        perimeter_func(l,b,h)
    return validity
    
@decor_triangle
def perimeter(l,b,h):
    sum=l+b+h
    print("Perimeter of a given triangle :",sum)

l=int(input("Enter length of a triangle :"))
b=int(input("Enter breadth of a triangle :"))
h=int(input("Enter height of a triangle :"))
perimeter(l,b,h)