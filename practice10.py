# highest and lowest marks print without useing max min method
student={"arshika":85.80,
         "rohan":78.0,
         "aman":56.0,
         "raman":89.94,
         "suman":91.0,
         "Arjun":86.78}
highest=0

lowest=100
for key,value in student.items():
    if highest < value:
        highest=value
        print(key)
    elif lowest > value:
        lowest=value  
        store=key
       
print("highest marks =",key,highest) 
print("lowest marks =",key,lowest)  

