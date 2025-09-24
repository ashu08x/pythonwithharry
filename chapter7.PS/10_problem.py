#write a program using for loop of multiplication table in reverse order
n=int(input("Enter you numbrer :"))
for i in range(1,11):
    print(f"{n} x {11-i} = {n *(11-i)}")
    i+=1

'''

    1 10
    2 9
    3 8
    4 7
    5 6
    6 5
    7 4
    8 3
    9 2  


'''