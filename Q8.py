# Question 8: Check the number is an Armstrong no
n = int(input("enter a num:"))
original = n
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit**3
    n = n // 10
if sum == original:
    print("Armstrong number:")
else:
    print("Armstrong number invalid:")
