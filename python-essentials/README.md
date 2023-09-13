Hello Friends

This folder contains my learning journey on python.
I used materials from cisco networking academy, and lots of youtube videos mainly Free code camp.

rock-paper-scissors
This is just a small game i made using some of the things i have learned below.


in this file we lean how to create variables and strings and call functions.

we first create  a function: this is a set of code that only works when called.
a function starts with def and ends with a colon.

Then we assign to the function variable called player_choice then assign a string rock
strings can either be in single or double qoutes
we now call the get_choices function and print its output.
eg: choices = get_choices()
print(choices)

FUNCTIONS
- This is a set of code that only works when called.
- For a function to work it need to be called
- Functions can accept different parameters. and the parameter becomes a variable that can be used.
- Parameters - are values accepted by the function inside the function definition
- Arguments - are values we pass to the function when we call it.
- Functions can also be nested in other functions. nested functions are only visible in that particular function

CLOSURE
- allows a function to remember the environment in which it was created and access variables from that environment, even after the enclosing function has finished executing.

OBJECTS(instances)
- everything is an object.
- they have attributes and methods

DICTIONARIES
- They are used to store data values in key value pairs
- it uses curly braces
eg: dict = {"name": "beau", "color": "blue"}
- in this case name and color are the key while beau and blue are the values
- the value can also be a variable
eg: dict = {"name": "beau", "color": choices}
- when sorounded by quotes it meants its a string if not it is a variable.
- key can be any value eg a string, number or a tuple. also the value can be anything.

SETS
- Can be changed
- Almost like dictionaries.
- Thedifference is in a dict it has curly braces and a colon while sets has currly braces but is separates the items using a comma
eg: name = {"cindy", "jeby"}
- A set can not have 2 of the same items
- if you combine 2 sets that have the same name in common it will only print it once.


 USER INPUT
 we use input() to ask the user to give as there input.

 to ask the computer for input we need libraries, lists, methods
 1. Libraries
 this are a set of usefull functions that help you not to write code from cratch.

for this we are going to use the random library. we will import it

2. Lists (lists.py)
- it is used to store multiple items in a single variable
they are surrounded by brackets and each item is separated by a comma
- eg: food = ["pizza", "carrots", "eggs"]
- here food is the variable and the items are in the brackets
- we use the "in" operator to chech for items in a list.

-> List Compressions


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

10. Tuples (lists.py)
- They allow one to create an emmudable groups of objects.
- Once created can not be changed,added or removed
- Other than that everything else works the same as lists
- You can create a new touple from the old one and add new items into it while creating it


VARIABLE.py
a variable name can contain anything in it. number or name
to make it it can have number init name but not at the begining.
eg: name_1 = age this is avariable that is assigned a value age

GLOBAL  AND LOCAL VARIABLES
- Global -> Are declared outside of a function hence can be used in anypart of that program.
- Local -> Are declared inside of afunction and can onlybe used in that function.

EXPRESSIONS AND STATEMENTS
expression is any code that returns a value
statement is an operation of a value

COMMENTS
we use the hash sign to make comments in python.
everything after the hash is not run as code .

DATA TYPES
to check what type of data type :
lets say we want to check name = "cindy" what data type this is we run print(type(name)) the output will be str which means string

OPERATORS.PY
1. Assing operator: is the eqaul sign =
2. Arithmetic operators: +, -, *, /, 
3. Comparison oparators: ==, !=, >, <, <=, >=
4. Boolean operators: not, and, or
   . Not- is used when something is not true
   . And - is used when both conditions are true, if one is not true the output of the whole thing is false
   . or - if either of the conditions is true the output is true.
5. Bitwise operators: &(and), |(or), ^(xor), ~(not), <<(shift left), >>(shift right)
6. Is & in operators:
   . is - thisis theidentity opeartor. it compares two objects and returns true if both objects are the same.
   . in - used to identify if a value is contained in another list or sequence.
7. ternary operator: 
basically this is its structure:
      def is_adult(age):
           return True if age > 18 else False

NUMBER DATA TYPES
complex number: all numbers are expressed as a sum of a real part and imaginary part

ENUMS
readable names that are bound to a constant value
to use it you have to import it
eg: from enum import Enum

STRINGS
this is a series of characters enclosed in a single or double qoutes
eg: "cindy", 'cindy', "20", '20' 
\n: new line
1. string characters & slicing
      . eg: name = "cindy is cool"
            print(name)
    to get a specific character we use index:
    index[o, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    name [c, i, n, d, y, i, s, c, o, o, l]
    so to get a specific char we can print(name[3])and the output will be [d],
    also to get say the last letter we can print(name[-1]) the output will be [l]

LOOPS
1. While loop
      - are defined using while
      - they repeat the loop until the outcome is False.
2. For loop
      - commonly used to repeat items in a list.
      - or can use range function to specify  the number of times it should repeat
      - we use enumerate to return the index of the list

      . CONTINUE & BREAK
      ->both while and for loops can be interapted using break and continue.
      -> continue: tells python to stop the current iretaration and tells it to continue to the next
      -> break: stops the loop 

CLASSES
- according to chat gpt: a class is a blueprint for creating objects.
- it defines a set of attributes and methods that the objects of the class will have.
- special type of method called "__init__" which is a constructor.
- classes can also inherite from each other.

MODULES
- Every python file is a module, one can import a module from a file
- Helps in code reuse
- Eg: if you have to files say first.py and second.py and you want to use first.py in second.py you import in to the second.py by adding this line of code into the socond.py file [import first.py], then call a specific function say [first.laptop()]
- Also you can import by saying [from first import laptop], this also imports a specific function from the first.py file to the second.py file, then tocall the specific function say [laptop()]
- Also say you have first.py in a sub folder called sub, an you want to import it to second.py which is not in the subfolder, in second.py you write this line of code [from lib import first] then to call the specific folder we use [first.laptop()]
- or on the same you can just say [from lib.first import laptop] then to call it use [laptop()]

- there are also STANDARD MODULE that have already been intergrated in python that you can import easily
eg: math, random, json, datetime and many more.

COMMAND LINE AKA TERMINAL.

LAMBDA FUNCTIONS (operations.py)
- are also called anonymous functions
- Defined using the lambda key word
- used when you need a quick, throwaway function for a short task
- its syntax: lambda argument : expression
- lambda functions are sometimes used with functions that accept other functions eg: map(), filter(), sorted(), reduce()
- To use reduce we have to import it first.

RECURSION
- we use a factorial.

DECORATORS (functions.py)
- is a way to change, inhance or alter in any way how a function works.
- They are defined with the @ symbol followed by the decorator name just before the function definition.

DOCSTRINGS
- Something like comments, reminds you what the code was supposed to do.
- We put the description in btwn 3 double quotes

ANNOTATION
- Are a way to provide additional information about the arguments and return values of functions.
- Annotations are optional and are specified using colons (:) after the parameter or return value, followed by an expression or type hint.
- They can be used to clarify the expected types or purposes of function arguments and return values.
- python generally iggnors this annotations

EXCEPTIONS
- Is a way to handle errors in python
- you can add some except block to check if there is a specific error in that code block