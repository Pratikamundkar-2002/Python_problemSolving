
# Find the second max Element in array

data= [2,3,56,8,34,6,5,98,4,34,3,12,5,4,5,4,32,45,56,98]

# new_list=set(data)
# largest=max(new_list)           # here we modify the list
# new_list.remove(largest)
# print(max(new_list))

#--------------------------------------------------------------------------

# sec_max=(sorted(set(data)))       # here we modify the list
# print(sec_max[-2])

#---------------------------------------------------------------------------

# fmax=data[0]
# smax=data[0]
# for i in data:
#     if i > fmax:
#         fmax=i
# for j in data:
#     if j >smax and j!=fmax:
#         smax=j
# print(smax)

#---------------------------------------------------------------------------

fmax=data[0]
smax=data[0]
for x in data:
    if x > fmax:
        smax=fmax
        fmax=x
    elif x > smax and x!=fmax:
        smax=x
print(smax)

        
