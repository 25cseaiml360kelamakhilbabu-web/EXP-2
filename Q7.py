# Question 7: Enter a word and check whether it is palindrome.
word = input("enter a word")
reverse = word[::-1]
if word == reverse:
    print("The word palindrom:")
else:
    print("not palindrome")
