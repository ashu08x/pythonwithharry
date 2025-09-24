status=()
#Assumed all three Subjects total marks each is 100)
marks1= int(input("Enter Your Marks1 :"))
marks2= int(input("Enter Your Marks2 :"))
marks3= int(input("Enter Your Marks3 :"))

#total Percentage
total_percentage=(100*(marks1+marks2+marks3))/100

if(marks1>=33 and marks2>=33 and marks3>=33 and total_percentage>=40):
    status="You Passed"
else:
    status="Failed, Try Next Time"

print("Status :", status)
