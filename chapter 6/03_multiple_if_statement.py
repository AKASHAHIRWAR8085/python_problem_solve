a=int(input("Enter your age: "))

# if statement number 1
if(a%2==0):
    print("You are entering an even age")

# if statement number 2
if (a >= 18):
    print("You are above the age of consent.")
    print("good for you")
elif(a<0):
    print("you are entering an invalid negative age")

elif(a==0):
    print("you are entering 0 which is not a valid age")    


else:
    print("You are below the age of consent.")
    
print("end of the program")            