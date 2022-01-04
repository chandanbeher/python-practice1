#1. Accept two integer values from the user and return their product. If the product is greater than 1000, then return their sum

a=int(input("Enter the a value"))
b=int(input("Enter the b value"))
c=a*b
print(c)
if c>1000:
    print("c is grater than 1000")
    sum=a+b
    print(sum)
