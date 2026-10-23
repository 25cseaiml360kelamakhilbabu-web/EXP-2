# Question 2: WAP to enter a five digit number and print the digits present at odd locations
n = int(input("enter 5 digit numbers:"))
print("Digit present at odd location:")
for i in range(5):
    if i % 2 == 0:
        print(n[i], end=" ")
