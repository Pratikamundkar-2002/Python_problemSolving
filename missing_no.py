 # Find missing no in a Array..

arr=[]
a=int(input("Enter length of array :"))


for i in range(a-1):
    ele=int(input("Enter elements :"))
    arr.append(ele)

total= a * (a+1) // 2
actual= sum(arr)

print("Missing number =", (total-actual))