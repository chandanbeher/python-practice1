num=int(input("enter the number:"))
fact=1
if num<0:
    print("sorry can not find")
elif num==0:
    print("sorry can not find")
else:
    for i in range(1,num+1):
        fact=fact*1
print(fact)