# Question 5: WAP to enter a number and check whether the number is perfect no or not.   
n = int(input("enter a number:"))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("number is perfect:")
else:
    print("number is not perfect")
