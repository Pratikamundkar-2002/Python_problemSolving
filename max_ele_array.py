# Find max element in array

elements=[2,3,4,2,13,5,533,5,23,1,7,56,34,23,5,68,86]

# print(max(Elements))


# Elements.sort()
# print(Elements[-1])



# without built-in method
max=elements[0]
for i in range (1,len(elements)):
    if max < elements[i]:
        max= elements[i]
print(max)