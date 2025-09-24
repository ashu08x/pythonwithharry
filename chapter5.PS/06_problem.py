'''
d = {
    input("Name1 :") : input("Fav lang1 :"),
    input("Name2 :") : input("Fav lang2 :"),
    input("Name3 :") : input("Fav lang3 :"),
    input("Name4 :") : input("Fav lang4 :"),
}'''

d= {}
name= input("Enter Your Name :")
lang= input("Enter Fav LAng :")

d.update({name : lang })
name= input("Enter Your Name :")
lang= input("Enter Fav LAng :")

d.update({name : lang })
name= input("Enter Your Name :")
lang= input("Enter Fav LAng :")

d.update({name : lang })
name= input("Enter Your Name :")
lang= input("Enter Fav LAng :")

d.update({name : lang })
print(d)