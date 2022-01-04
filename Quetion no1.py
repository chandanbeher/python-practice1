str=input("Enter the string: ")
words=str.split(" ")
count=1
for i in range(len(words)):
   for j in range(i+1,len(words)):
      if words[i]==words[j]:
         count=count+1
         words[j]=None
   if count>1 and words[i]!=None:
      print(words[i])
   count=1