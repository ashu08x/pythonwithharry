n = int(input("Enter your number : "))

if n <= 1:
    status = "Number is not Prime"
else:
    for i in range(2, n):
        if n % i == 0:
            status = "Number is not Prime"
            break
    else:
        status = "Number is Prime"

print(status)

   

# 1 follows the criteria but not prime
