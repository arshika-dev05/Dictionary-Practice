student={"Arshika":89,"ravi":79,"rohan":81,"aman":45} 
highest=max(student.values())
for name,marks in student.items():
    if marks == highest:
        print(f"{name}:{marks}")
 
 