#Remove Duplicate Elements from sorted Array 
lst=[1,3,4,2,6,8,2,1,1]
srt=sorted(lst)
print("Sorted array",srt)
rem_dup=set(srt)
print("Sorted array without duplicates is",list(rem_dup))
