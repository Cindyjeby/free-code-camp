Hello Friends

This folder contains my learning journey on python.
I used materials from cisco networking academy, and lots of youtube videos mainly Free code camp.

rock-paper-scissors
in this file we lean how to create variables and strings and call functions.

we first create  a function: this is a set of code that only works when called.
a function starts with def and ends with a colon.

Then we assign to the function variable called player_choice then assign a string rock
strings can either be in single or double qoutes
we now call the get_choices function and print its output.
eg: choices = get_choices()
print(choices)

DICTIONARIES
they are used to store data values in key value pairs
it uses curly braces
eg: dict = {"name": "beau", "color": "blue"}
in this case name and color are the key while beau and blue are the values
the value can also bea variable
eg: dict = {"name": "beau", "color": choices}
 when sorounded by quotes itmeants its a string if not it is a variable and in this example it calls line 7.

 USER INPUT
 we use input() to ask the userto give as there input.

 to ask the computer for input we need libraries, lists, methods
 1. Libraries
 this are a set of usefull functions that help you not to write code from cratch.

for this we are going to use the random library. we will import it

2. Lists
it is used to store multiple items in a single variable
they are surrounded by brackets and each item is separated by a comma
eg: food = ["pizza", "carrots", "eggs"]
here food is the variable and the items are in the brackets

3. Arguments
functions can receive data this data is called an argument

4. if statement
allows a computer to do different things deppending on the program.

5. Concatenating stings
is a way to combine strings with other strings or variables
eg: print("You Chose: " + player + ", Computer Chose: " + computer)

6. F string
is also away of combining strings with variables.
eg: age = 25 we ahve assigned string 25 to variable age
print(f"he is {age} years old.")
f string is a simple way to concatenate strings and variables

7. else and elif

8. Refactoring and nested if
refactoring is the proccess of restructuring code while keeping the same functionality

9. How to access something specific in a dictionary
lets say we have a dictionary :
choices = {"player": "rock", "comuper": "paper"}
to access lets say only the players choice we say
p_choice = choices["player"]