age=int(input("Enter the age:"))
weight=int(input("Enter the weight:"))
if age>=18:
    if weight>=50:
        print("your eligible for doneate blood:")
    else:
        print("under weight")
else:
    print("under age")
    