#Plus one
lst=[]
n=int(input("Enter the number of elements to be entered"))
for i in range(n):
    num=int(input("Enter the element"))
    lst.append(num)
print(lst)
lst2=[]
for i in range(n):
    if i==n-1:
        lst2.append(lst[i]+1)
    else:
        lst2.append(lst[i])
print("Plus one",lst2)
