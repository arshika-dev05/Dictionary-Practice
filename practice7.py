student={1:"arshika",
         2:"juhi",
         3:"aku",
         4:"rahim",
         5:"raman",}
print("total student=",student)

delete_student=int(input("enter roll no for remove student = "))
delete=student.pop(delete_student)
print(f"deleted student={delete}")
print(f"now student={student}")