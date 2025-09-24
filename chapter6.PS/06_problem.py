grade=()
marks=int(input("Enter Your Marks :"))

if(90<=marks<=100):
    grade="Ex "
if(80<=marks<90):
    grade="A"
if(70<=marks<80):
    grade="B"
if(60<=marks<70):
    grade="C"
if(50<=marks<60):
    grade="D"
if(marks<50):
    grade="f"

print(grade)