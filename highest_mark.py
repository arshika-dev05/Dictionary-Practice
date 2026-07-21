# highest markes
student={"Rohan":87,
         "sonam":78,
         "Rahul":81,
         "irfan":89,
         "Samir":67,
         "Aman":46
         }
# all_values=student.values()
highest=student.get("Rohan")
for name,marks in  student.items() :
    if marks > highest:
        highest = marks
        highest_name = name
print(f"{highest_name} = {highest}")        

