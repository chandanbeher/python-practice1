def primenumber(num):
    flag=false
    if num>1:
        for i in range(2,num):
            if num%i==0:
                flag=true
                break
    if flag:
        print(num,"not a prime number")
    else:
        print(num,"is a prime number")
    num=int(input("enter the number:"))
    primenumber(num)