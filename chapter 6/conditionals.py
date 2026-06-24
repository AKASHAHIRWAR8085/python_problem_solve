# conditional expressions -:
# A Conditional Expression (also called the Ternary Operator) is a one-line shortcut for an if-else statement.
 
# 01  example of conditional expression

# a=int(input("Enter your age: "))
# result = "You are eligible to vote." if a >= 18 else "You are not eligible to vote."
# print(result)

a=int(input("Enter your age: "))
if (a >= 18):
    print("You are above the age of consent.")

    print("good for you")
elif(a<0):
    print("you are the blow of the age og consent")


else:
    print("You are below the age of consent.")
print("end of the program")            