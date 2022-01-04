#3. Ron has been given 10 numbers which includes both positive and negative values by his teacher. His task is to tell the total of positive and negative numbers separately. Our task is to help him in this task.
i = 1
p = 0
ne = 0
for i in range(10):
    n = int(input("Enter Number:"))
    if n > 0:
        p = p+n 
    elif n < 0:
        ne = ne +n
print("Sum of negatives :",ne)
print("Sum of Positive Number :",p)