
# Count Occurance of each element in an Array/list

arr=[1,2,3,4,5,2,3,6,4,6,5,7,8,4,1,1,1]

d={}
for ele in arr:
    if ele in d:
        d[ele]+=1
    else:
        d[ele]=1
print(d)

#---------------------------------------------------------------------------

#count occurance of given element in array/list

a=int(input("enter element :"))
counter=0
for num in arr:
    if(num==a):
        counter+=1
print(f"{a} has occured {counter} times")
