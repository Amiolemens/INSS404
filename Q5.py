grades = []
for i in range(3):
       grade = float(input("Enter the final grade for student{}:".format(i+1)))
       grades.append(grade)

average_grade = sum(grades) / len(grades)

if average_grade >=90:
       letter_grade = "A"
elif average_grade >=80:
       letter_grade = "B"
elif average_grade >= 70:
       letter_grade = "C"
elif average_grade >= 60:
       letter_grade = "D"
elif average_grade >= 50:
       letter_grade = "E"
else:
       letter_grade = "F"

print("Average grade is",average_grade)
print("Final letter grade is :", letter_grade)