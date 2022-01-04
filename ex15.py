num=[23,43,54,12,43,45,65]
count=1
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]==num[j]:
            count=count+1
            num[j]=None
    if count>1 and num[i]!=None:
        print(num[i])
    count=1            