#Write a program to find common elements in two arrays
lst1=[1,2,3,4,5]
lst2=[5,6,7,8,9]
s1=set(lst1)
s2=set(lst2)
print(s1,s2)
common=s1.intersection(s2)
print("Common elements in an array are", list(common))
