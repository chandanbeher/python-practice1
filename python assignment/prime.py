num=int(input("enter the num:")
for i in range(2,num):
    if(num%i==0):
        count=count+1
        break;
    if(count==0):
        print("0")
    else:
        print("n")
        