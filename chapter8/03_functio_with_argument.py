'''
name=input("Enter your name :") 
def goodday(name):
    print("Good Day, " + name)
    print("Thank You")
goodday(f"{name}")'''


name=input("Enter your name :") 
def goodday(name):
    print("Good Day, " + name)
    print("Thank You")
    return "NIce to Meet You!"
a=goodday(f"{name}")
print(a)