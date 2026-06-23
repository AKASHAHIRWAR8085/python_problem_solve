# 01 wap to store saven fruits in a list enterd by the user
# fruits=[] 
# for i in range(7):
#     fruit=input("Enter the name of the fruit: ")
#     fruits.append(fruit)
# print("The list of fruits is:", fruits)

# 02 wap to accept marks of 6 students and disply them in a sorted manner
# marks=[]
# for i in range(6):
#     mark=int(input("Enter the marks of the student: "))
#     marks.append(mark)
# marks.sort()
# print("The sorted marks are:", marks)

# 03 check that a type cannot be changed in python
# a=10
# print(a)
# print(type(a))
# a="Aakash"
# print(a)
# print(type(a))

# wap to sum list with 4 numbers
# numbers=[]
# for i in range(4):    
#     number=int(input("Enter a number: "))
#     numbers.append(number)
# total=sum(numbers)
# print("The sum of the numbers is:", total)

#  wap to count the number of zero in the following tuple
a=(1,0,2,0,3,0,4,5)
print(a)
no=a.count(0) # count() method is used to count the number of occurrences of an item in the tuple
print("The number of zeros in the tuple is:", no)
