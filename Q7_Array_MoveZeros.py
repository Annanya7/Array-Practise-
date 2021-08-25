#Move Zeros
nums = [0,1,0,3,12]
lst2=[]
zero=[]
for i,ele in enumerate(nums):
    print(i,ele)
    if ele==0:
        lst2.append(i)
print("positions of zeros",lst2)
for i in range(len(lst2)):
    nums.remove(0)
print(nums)
for i in range(len(lst2)):
    nums.append(0)
print("Move Zeros",nums)
