num={21,24,36,87,43,90,63}
max=0
smax=0
for i in num:
    if max<i:
        smax=max
        max=i
    elif i<smax:
        smax=i
print("maximum number :",max)
print("small maximum number :",smax)    