# Lowest marks
students={"Rohan":87,
         "sonam":78,
         "Rahul":81,
         "Samir":67,
         "Aman":46,
         "irfan":89,
         "Raj":41,
         }
lowest=students.get("Rohan")
# lowest_student = "Rohan"
for student,marks in students.items():
    if marks < lowest:
        lowest=marks
        lowest_student=student
print(f"{lowest_student} = {lowest}") 
       