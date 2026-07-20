# sum number 
number={"num1":10,
        "num2":20,
        "num3":27,
        "num4":34
        }
all_values=number.values()
all_keys=number.keys()
count=0
for x in all_values:
    count+=x
print("sum num =",count)    