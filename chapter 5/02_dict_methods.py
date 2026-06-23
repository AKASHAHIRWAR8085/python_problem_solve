# Dictionary Methods
# 1 - items() method
# mark = {
#     "Aakash": 85,
#     "Rohit": 90,
#     "Suman": 78,
#     "Priya": 92,

# }
# print(mark.items()) # items() method is used to return a view object that displays a list of a dictionary's key-value tuple pairs.

# 2 - keys() method
# mark = {
#     "Aakash": 85,
#     "Rohit": 90,
#     "Suman": 78,
#     "Priya": 92,
# }
# print(mark.keys()) # keys() method is used to return a view object that displays a

# list of all the keys in the dictionary.
# 3 - values() method
# mark = {  
#     "Aakash": 85,
#     "Rohit": 90,      
#     "Suman": 78,
#     "Priya": 92,
# }
# print(mark.values()) # values() method is used to return a view object that displays a list of all the values in the dictionary.


student = {
    "name": "Akash",
    "age": 22
}

# get()
print(student.get("name"))

# keys()
print(student.keys())

# values()
print(student.values())

# items()
print(student.items())

# update()
student.update({"city": "Bhopal"})
print(student)

# pop()
student.pop("age")
print(student)
  