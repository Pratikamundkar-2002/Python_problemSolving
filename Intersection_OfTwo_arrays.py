# find intersection of two Arrays and remove duplicates

sum1=[1,2,3,2,4]
sum2=[0,2,5,2]

# a=set(sum1)
# b=set(sum2)
# print(a & b)

#-----------------------------------------------

intersection=[]
for i in sum1:
    if (i in sum2 and i not in intersection):
        intersection.append(i)
print(intersection)

#=-------------------------------------------------------------

