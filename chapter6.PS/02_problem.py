
Status=()
physicstotal=int(input("Enter Physics Total Marks :"))
chemistrytotal=int(input("Enter Chemistry Total Marks :"))
mathstotal=int(input("Enter Maths Total Marks :"))
total= physicstotal+chemistrytotal+mathstotal

physicsmarks=int(input("Physics Marks :"))
chemistrymarks=int(input("Chemistry Marks :"))
mathsmarks=int(input("Maths Marks :"))

totalmarks= physicsmarks + chemistrymarks + mathsmarks
print("Total Marks Obtained :", totalmarks)


pget=[]
physicsper= (physicsmarks*100)/physicstotal
Chemistrtyper= (chemistrymarks*100)/chemistrytotal
mathsper= (mathsmarks*100)/mathstotal
totalper= (totalmarks*100)/total

a= (physicsper, Chemistrtyper, mathsper, totalper)
pget.extend(a)

print("Percentages :", pget)

if(physicsper>=33 and Chemistrtyper>=33 and mathsper>=33 and totalper>=40):
    Status= "Pass"
else:
    Status="Fail"

print(Status)








#((physicsmarks and chemistrymarks and mathsmarks and totalmarks)*100 / physicstotal and chemistrytotal and mathstotal and total)
