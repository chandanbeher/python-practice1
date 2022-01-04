#6. Write a Python program to check whether the given number is a Palindrome or not.
#Palindrome -> the number is equal to the reverse of the number

rev=0
n=int(input("enter n value:"))
temp=n;
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if temp==rev:
    print("palindrome")
else:
    print("zero")