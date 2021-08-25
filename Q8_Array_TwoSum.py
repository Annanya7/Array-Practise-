nums = [3,2,4]
lst=[]
target = 6

for i in range(len(nums)):
    j=i+1
    if nums[i]+nums[j]==target:
        print(nums[i]+nums[j])
        lst.append(i)
        lst.append(j)
        break
    else:
        pass
print(lst)
        
