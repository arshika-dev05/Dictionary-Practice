# highest markes
student={"Rohan":87,
         "sonam":78,
         "Rahul":81,
         "Samir":67,
         "Aman":46,
         "irfan":89
         }
# all_values=student.values()
highest=student.get("Rohan")
name1="Rohan"
print(name1)
for name,marks in  student.items() :
   
    if marks > highest:
        highest=marks
print(f"{name1} = {highest}")        

