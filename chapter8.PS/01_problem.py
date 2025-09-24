#write a program using function to find out greatest of 3 number
def greatest():
    n1=int(input("Enter your number :"))
    n2=int(input("Enter your number :"))
    n3=int(input("Enter your number :"))
    if(n1>n2 and n1>n3):
        print("Greatest number :", n1)
    elif(n2>n1 and n2>n3):
        print("Greatest number :", n2)
    elif(n3>n1 and n3>n2 ):
        print("Greatest number :", n3)

greatest()