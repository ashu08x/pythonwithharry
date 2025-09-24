# write a python function which convert inches to cm
'''
def covert():
    n=int(input("Enter no. in inches : ")) 
    print(f"{n} inch = {n*5/2} cm")

covert()'''

def inch_to_cms(inch):
    return inch * 2.54
n =int(input("Enter no. in inches : "))

print(f"{n} inch = {inch_to_cms(n)} cm") 