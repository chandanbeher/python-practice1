num=int(input("Enter the number:"))
count=0
for i in range(2,num):
    if(num%i==0):
        count=count+1
        break;
if count==0:
    print("prime")
else:
    print("not")