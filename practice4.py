# subtraction
number={  }
no1=int(input("Enter num1 = ",))
number.update({"num1":no1})
no2=int(input("enter num2 = "))
num2=number.update({"num2":no2})
print(number)
sub1=number.get("num1")
sub2=number.get("num2")
print("subtraction =",sub1-sub2)
