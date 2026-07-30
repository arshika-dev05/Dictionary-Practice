# highest and lowest marks print without useing max min method
student={"arshika":85.80,
         "rohan":78.0,
         "aman":56.0,
         "raman":89.94,
         "suman":91.0,
         "Arjun":86.78}
highest=0
highest_student_name=""
lowest=100
lowest_student_name=""

for key,value in student.items():
    if highest < value:
        highest=value
        student_name=key
    elif lowest > value:
        lowest =value
        lowest_student_name=key

print("highest marks =",student_name,highest) 
print("lowest marks =",lowest_student_name,lowest)  

