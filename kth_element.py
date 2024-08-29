
list=[2,4,2,6,8,3,5,7,9,12,34,56,23,12,34,56]
k=int(input("K ="))

# Find Kth SMALLEST Element in an list :

new_list=sorted(set(list))
print(new_list[k-1])


# find Kth LARGEST element in list :

new_list2=sorted(set(list),reverse=True)
print(new_list2[k-1])