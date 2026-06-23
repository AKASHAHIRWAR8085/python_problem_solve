# write a python program to display a user entered name followed by good afternoon using input() function
# name = input("Enter your name: ")
# print(f"Good Afternoon, {name}!")

#  write a program to fill in a letter template given name and date
# letter =  '''Dear <|NAME|>,
#             You are worn out!
#             <|DATE|>'''
# print(letter.replace("<|NAME|guble space in a strin>", "Aakash").replace("<|DATE|>", "2003-06-15"))

#  write a program to detect double spaces in a string
name = "Aakash  Singh"  # Example string with double space
# print(name.find("  "))  # This will return the index of the first double space
# print(name.replace("  ", " "))
# print(name)  strings are immutable in python, so the original string will not change unless we assign the modified string back to the variable
name = name.replace("  ", " ")  # Now we assign the modified string back to

#  write a program to format the following letter using escape sequence characters
letter = " Dear Aakash,\n\tYou are doing good in python.\n\tKeep it up!\n\nRegards,\nYour Teacher"
print(letter)