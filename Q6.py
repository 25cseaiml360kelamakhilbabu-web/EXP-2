# Question 6: Enter a 3 digit number and print all prime factors.
n = int(input("enter a 3 digit number:"))
print("prime factors", end=" ")
i = 2
while i <= n:
    while n % i == 0:
        print(i, end=" ")
        n = n / i
    i += 1
