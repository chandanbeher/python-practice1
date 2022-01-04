str=input("Enter the string:")
words=str.split(" ")
for i in range(len(words)-1,-1,-1):
    print(words[i],end=" ")