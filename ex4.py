nums=[]
for j in range(5):
    nums.add(int(input("Enter the number:")))
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            temp=nums[j]
            nums[i]=nums[j]
            nums[j]=temp
print(nums)
    