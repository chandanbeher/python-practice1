str=input("Enter the string:")
words=str.split(" ")
count=0
dcount=0
scount=0
for word in words:
    for ch in word:
        if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
            count=count+1
        elif ch>='0' and ch<='9':
            dcount=dcount+1
        else:
            ch!=''
            scount=scount+1
print("Number of character: ",count)
print("Number of digits: ",dcount)
print("Number of special characer: ",scount)