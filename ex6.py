str=input("enter the string:")
words=str.split(" ")
count=0
dcount=0
scount=0
for i in range(len(words)-1,-1,-1):
    print(words[i],end=" ")
for ch in str:
    if ch>='0' and ch<='9':
        count=count+1
    elif ch>='a' and ch<='z' or ch>='A' and ch<='Z':
        dcount=dcount+1
    elif ch!=' ':
        scount=scount+1
print("number:",count)
print("number:",dcount)
print("number:",scount)
    