#average of grades

courses=[]
for i in range(3):
    courseName=input("Course:")
    courses.append(courseName)
print("Student courses are:",courses)

grades=[]
grade1=float(input("Grade of course1:"))
grade2=float(input("Grade of course2:"))
grade3=float(input("Grade of course3:"))
sum=0.0
grades.append(grade1)
grades.append(grade2)
grades.append(grade3)
sum=grades[0]+grades[1]+grades[2]
average=sum/3
print("Student average is:",average)
    
