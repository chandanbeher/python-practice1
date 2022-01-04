num=133
count=len(str(num))
sum=0
while(num!=0):
    rem=num%10
    sum=sum+rem**count
    num=num//10
if temp==sum:
    print("amstrong")
else:
    print("not amstrong")
        
    