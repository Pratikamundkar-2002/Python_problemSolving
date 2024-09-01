
#------------------------ Merge 2 list --------------------------------

lst1=[3,4,6,8,5]
lst2=[7,8,9,2,3,5]

# lst3=lst1+lst2
# print(lst3)

#---------------------------

for i in lst2:
    lst1.append(i)
print(lst1)

#=============================================================================

# ------------------- Merge 2 sorted list --------------------------
l1=[1,3,5,7,8]
l2=[2,3,4,6,8,9,10,12,15]

print(sorted(l1 + l2))

#---------------------------------

# for i in l2:
#     l1.append(i)
# print(sorted(l1))

#---------------------------------

size_1 = len(l1)
size_2 = len(l2)
res = []
i, j = 0, 0
while i < size_1 and j < size_2:
    if l1[i] < l2[j]:
        res.append(l1[i])
        i += 1
    else:
        res.append(l2[j])
        j += 1
res = res + l1[i:] + l2[j:]
print("The combined sorted list is : ",res)






