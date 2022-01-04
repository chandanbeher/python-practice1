rev=0
num=int(input("Enter the number:"))
temp=num;
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")