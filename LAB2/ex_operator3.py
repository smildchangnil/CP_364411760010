"""
Name: Kanyanat Changnil
ID: 364411760010
Group: MIT421


"""

#logical operators
x,y,z = 10,20,30
#and
print(x>y and y<z)  # f and t --> f
print((x and (y==z)) and (y and (y==x)))
#or
print(x==10 or x==100)
#not
print(not(not(x==10 or x==100))) #F

print(not(not(x==10 or x==100)) and x!=y or y==z)