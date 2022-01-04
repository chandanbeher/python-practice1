str=input("Enter the string:")
str1=input("Enter the string:")
count=0
if len(str)<len(str1):
    for i in range(len(str)):
        if str[i]==str1[i]:
            count=count+1
print(count)
else:
    for i in range(len(str)):
        if str[i]==str1[i]:
            count=count+1
            print(count)