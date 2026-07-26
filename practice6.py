# add new student in dictionary     
student={ }
print(student)
plus=1
add_student=input("add new name = ")
student.update({plus:add_student})
plus+=1
 
while not type=="no":
    type=input(" if you want to add one more student name type 'yes' otherwise type 'no' = ").lower()
    if type=="yes":
        add_student=input("enter name = ")
        student.update({plus:add_student})
        plus+=1    
    elif type == "no":
        print("ok") 
    else:
        print("sorry you type wrong latter type 'yes' or 'no' ")    
print("add new student =",student)            

 