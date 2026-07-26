# search student marks
student={"arshika":85.80,
         "rohan":78.0,
         "aman":56.0,
         "raman":79.60,
         "suman":81.0,}
user=input("enter name for searching marks = ")
for key,value in student.items():
    if key == user:
        print(f"{key}={value}")
