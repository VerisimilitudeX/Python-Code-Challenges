num = int(input("Enter a number: "))
factors = []
divisor = 2
if num == 1:
    print("1 is not a prime number")
while divisor <= num:
    if num % divisor == 0:
        factors.append(divisor)
        num = num / divisor
    else:
        divisor += 1
print(factors)