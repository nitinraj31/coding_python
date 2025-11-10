n=int(input("Enter the no of student in the class"))
for i in range(n):
    name=input("Enter the name of students:")
    roll_no=int(input("Enter the roll  no  of students:"))
    father_name=input("Enter the father name of students:")
    mother_name=input("Enter the mother name of students:")
    marks=int(input("enter the marks obtained by the students :"))
    print("The name of students is :",name.capitalize())
    print("The roll no of students is :",roll_no)
    print("The father name of students is :Mr.",father_name.capitalize())   
    print("The mother name of students is :Mrs.",mother_name.capitalize())
    print("The marks obtained by the students is :",marks)  

