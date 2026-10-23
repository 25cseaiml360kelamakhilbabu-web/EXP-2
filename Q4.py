# Question 4: WAP to enter a string and print it in reverse. print the no of vowels and consonent in it.
a = str(input("enter a string:"))
reverse = a[::-1]
print("Reversed string is:", reverse)
if a in "aeiou AEIOU":
    print("It is a vowel:")
else:
    print("It is a consonent:")
