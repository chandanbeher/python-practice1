n=int(input("enter the number:"))
count=len(str(n))
temp=n
sum=0
while(n!=0):
    rem=n%10
    sum=sum+rem**count
    n=n//10
if temp==sum:
    print("amstrong")
else:
    print("not amstrong")