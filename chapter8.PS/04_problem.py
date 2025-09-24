#write a recursive function to 1st n natural number
#first n natral no.= 1 ,2, 3, 4....n
'''
def natural():
    n=int(input("Enter the number :"))
    for i in range(1,n+1):
        print("nth natural no. ", i)
        i += 1

natural()''' # my attempt but , where recursion i don't know & here recurssion don't use

'''
def sum():
    n=int(input("Enter the number :"))
    print(f"sum of first {n} natural no. =", (n*(n+1))/2)

sum()
'''
'''
def sum():
    n=int(input("Enter the number :"))
    return (n*(n+1)/2)

a=sum()
print("Sum of Nth NAtural No.",a)'''


# Now learn from harry

'''
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3

sum(n) = 1+2+3+4+5+6+......n-1 + n
sum(n) = sum(n-1) + n 
'''

#Recursion function khud ko call krta hai
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(4))



             

        