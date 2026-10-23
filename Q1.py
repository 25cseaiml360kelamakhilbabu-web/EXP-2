# Question 1: WAP to enter percentage and display the grading system.
per = int(input("enter the percentage:"))
if per >= 90 and per <= 100:
    print("grade: O")
elif per >= 80 and per <= 90:
    print("grade: A")
elif per >= 70 and per <= 80:
    print("grade: B")
elif per >= 60 and per <= 70:
    print("grade: C")
elif per >= 50 and per <= 60:
    print("grade: D")
elif per >= 40 and per <= 50:
    print("grade: E")
else:
    print("grade: fail")
