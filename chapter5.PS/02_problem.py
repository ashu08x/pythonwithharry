'''
l1=[]
n1=int(input("enter n1 :" ) )
n2=int(input("enter n2 :" ) )
n3=int(input("enter n3 :" ) )
n4=int(input("enter n4 :" ) )
n5=int(input("enter n5 :" ) )
n6=int(input("enter n6 :" ) )
n7=int(input("enter n7 :" ) )
n8=int(input("enter n8 :" ) )

l2= (n1, n2, n3, n4, n5 , n6, n7, n8)

l1.extend(l2)
l1.sort()

print(l1)'''

'''
s1= set()

n1=int(input("enter n1 :" ) )
n2=int(input("enter n2 :" ) )
n3=int(input("enter n3 :" ) )
n4=int(input("enter n4 :" ) )
n5=int(input("enter n5 :" ) )
n6=int(input("enter n6 :" ) )
n7=int(input("enter n7 :" ) )
n8=int(input("enter n8 :" ) )

s2={n1, n2, n3, n4, n5, n6, n7, n8}

print(s1.union(s2)) '''



s1=set()
n=int(int(input("Enter Number n1 :")))
s1.add(n)
n=int(int(input("Enter Number n2 :")))
s1.add(n)
n=int(int(input("Enter Number n3 :")))
s1.add(n)
n=int(int(input("Enter Number n4 :")))
s1.add(n)
n=int(int(input("Enter Number n5 :")))
s1.add(n)
n=int(int(input("Enter Number n6 :")))
s1.add(n)
n=int(int(input("Enter Number n7 :")))
s1.add(n)
n=int(int(input("Enter Number n8 :")))
s1.add(n)

print(s1)




