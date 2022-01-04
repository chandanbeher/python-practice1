#1.  Program for Adding, removing elements in the list.
list=[11,45,21,25,44]
n=int(input("enter the add value="))
list.insert(4,n)#add
print(list)
b=int(input("enter the remove value in given data [12,15,11,25,33]="))
list.remove(b)
print(list)