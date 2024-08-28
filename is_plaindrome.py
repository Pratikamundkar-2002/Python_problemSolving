
# check if the String is Plaindrome.

string=input("enter a string: ")
reverse= string[::-1]
if string == reverse:
    print("Is plaindrome")
else:
    print("Is not a plaindrome")