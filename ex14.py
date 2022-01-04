str=input("Enter the string: ")
words=str.split(" ")
count=0
for i in words:
    for ch in i:
        if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
            count=count+1
print(i," : ",count)
count=0