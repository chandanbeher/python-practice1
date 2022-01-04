str=input("enter string:")
acount=0
dcount=0
ccount=0
for ch in str:
    if ch=='a' ,ch=='e' ,ch=='i' , ch=='o' and ch=='u' or ch=='A' , ch=='E' , ch=='I' , ch=='O', ch=='U':
        acount=acount+1
    elif ch>='0' and ch<'9':
        dcount=dcount+1
    elif ch!=' ':
        ccount=ccount+1
print("number is alphabet: ",acount)
print("number is digit: ",dcount)
print("number is contains: ",ccount)
