#Contains Duplicate
nums = [1,1,1,3,3,4,3,2,4,2]
num=sorted(nums)
print(num)
for i in range(len(num)):
    if num[i-1]==num[i]:
        break
print("true")

