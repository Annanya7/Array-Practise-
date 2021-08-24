#How many times an element occured in an array
lst=[]
for i in range(10):
    num=int(input("enter the number"))
    lst.append(num)
print(lst)
n=int(input("enter the element to be searched"))
c=0
for i in lst:
    if n==i:
        c=c+1
print("The number of times",n,"occured is:",c)
