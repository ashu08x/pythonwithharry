''' 
  *     for n=3, if n=4 hota to three spaces se start krte
 ***
*****  

'''

n= int(input("Enter the number :"))
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"* (2*i-1), end="")
    print("")

