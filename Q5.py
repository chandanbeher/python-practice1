abc={'ram':90, 'prasad':45,'mahesh':50,'kiran':88,'srinu':90}
def returnSum(abc):
    list = []
    for i in abc:
        list.append(abc[i])
    final = sum(list)
     
    return final