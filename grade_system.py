# write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100: A+
# 80-89: A
# 70-79: B
# 60-69: C
# 50-59: D
# 0-49: F
en=int(input("Enter the marks obtained by the student in english  subject :"))
mth=int(input("Enter the marks obtained by the student in mathematics subject :"))
phy=int(input("Enter the marks obtained by the student in physics subject :"))
che=int(input("Enter the marks obtained by the student in chemistry subject :"))
total_marks = en + mth + phy + che
average_marks = total_marks / 4 
if(average_marks>=90 and average_marks<=100):
    print("Grade: A+")
elif(average_marks>=80 and average_marks<90):
    print("Grade: A")
elif(average_marks>=70 and average_marks<80):
    print("Grade: B")
elif(average_marks>=60 and average_marks<70):
    print("Grade: C")
elif(average_marks>=50 and average_marks<60):
    print("Grade: D")
elif(average_marks>=0 and average_marks<50):
    print("Grade: F")   
else:
    print("Invalid marks entered. Please enter marks between 0 and 100.")