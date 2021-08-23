#Rotating an array
lst1=[]
lst2=[]
nums = [1,2,3,4,5,6,7]
k = 3
for i in range(len(nums)):
    lst1.append(nums[i])
    if i==k:
        break
print(lst1)
for i in range(k+1,len(nums)):
    lst2.append(nums[i])
print(lst2)
lst2.extend(lst1)
print("rotated array",lst2)
        
