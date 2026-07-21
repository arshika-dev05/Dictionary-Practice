# highest markes
student={"Rohan":87,
         "sonam":78,
         "Rahul":81,
         "Samir":67,
         "Aman":46,
         "irfan":89
         }
# all_values=student.values()
for name,marks in  student.items() :
    highest=student.get("Rohan")
    if marks > highest:
        highest=marks
print(f"{name} = {highest}")        

