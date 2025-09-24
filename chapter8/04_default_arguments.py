'''
name=input("Enter your name :")
ending=input("Enter Salutation :")

def a(name , ending="Thank You"):
    print("Good Day", name)
    print(ending)
    a(f"{name}, {ending}")'''





def a(name , ending="Thank You"):
    print(f"Good Day, {name}")
    print(ending)

a("Harry" ,"Thanks")
a("Rohan")