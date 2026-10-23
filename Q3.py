# Question 3: WAP to enter a number and check whether if it is a palindrome number or not
num = int(input("enter a number:"))
rev = 0
ori = num
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if ori == rev:
    print("It is Palindrome")
else:
    print("It is not palindrome")
