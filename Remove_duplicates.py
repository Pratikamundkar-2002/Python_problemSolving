
# Remove duplicates from Array------

arr=[1,2,3,2,5,4,5,6,7,8,9]

result=[]

# for i in arr:
#     if i in result:
#         continue
#     else:
#         result.append(i)
# print(result)

#-------------------------------------------------

for i in arr:
    if i not in result:
        result.append(i)
print(result)