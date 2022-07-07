import re
palindrome = input("Enter a palindrome: ")
if re.search(r'[^A-Za-z0-9]', palindrome):
    print("Invalid input")
else:
    if palindrome == palindrome[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")