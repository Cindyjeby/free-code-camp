def hello(name, age):
    name = input("What is your name? ")#asks user for their name
    print("Hello " + name)#prints message with users input
    age = input("how old are you " + name + "? ")#asks user for there age
    print("You are " + str(age) + " years old!" + "\n")#prints the users input
hello("name", "age")#calls the function

#NESTED FUNCTIONS
def talk(phrase):#main function
    def say(word):#the nested function
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('My Name Is Cindy\n')

#NESTED FUNCTIONS AND CLOSURE
def counter():
    count = 0

    def increment():
        nonlocal count#used to access an outerfunction in the inner function
        count = count + 1
        return (count)
    return (increment)
increment = counter()
print(increment())#1
print(increment())#2
print(increment())#3