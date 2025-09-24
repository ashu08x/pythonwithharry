s= set()
s.add(20)
s.add(20.0)
s.add("20") #lenth of s after these operations

print(len(s))

#length is 2 instead of 3 is because in python 1==1.0 compaaring value not type
