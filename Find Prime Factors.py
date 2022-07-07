num = int(input("Enter a number: "))
factors = []
divisor = 2
if num == 1:
    print("1 is not a prime number")
elif num % divisor == 0:
    print(str(num) + " is a prime number")