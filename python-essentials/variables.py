age = 54.4 #age is a variable and 54.4 is a value assigned to it.
print(isinstance(age, float))#checks if the value in the variable age is a float.

name = "cindy" #name is the variable cindy is the value assigned to it
print(type(name))#checks the data type of the value in the variable name
print("\n")#prints new line

#examples for string charsand slicing
var = "cindy is cool"
print(var[:6])#returns everything until just before char 6
print(var[5:])#returns everything after char 5
print("\n")#prints new line

#user input
age = input("how old are you: ")
print("Your age is " + age)
print("\n")#newline

#conditional statements
condition = False
if condition == True:
    print("Yes it is True")
else:
    print("it is False")
print("\n")