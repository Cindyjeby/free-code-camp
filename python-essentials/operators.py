from functools import reduce

#Assign Operator
money = 20 #we use the eqaul sign to assign the value 20 to age

#arthmitic operators
print("arithmetic outputs:")
age = 8
age *= 8
print(age)

#complex numbers
print("complex numbers outputs:")
num1 = 2+3j
num2 = complex(2, 3)
print(num2.real, num2.imag)

#enums
print("enums outputs:")
from enum import Enum
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
print(State.ACTIVE.value)#prints 1
print(State.INACTIVE.value)#prints 0
print(list(State))
print(len(State))

#Int objects
print("int objects outputs:")
age = 8
print(age.real)
print(age.imag)
print(age.bit_count())
print(age.bit_length())
print("\n")

#Lambda Functions
print("lambda function outputs:")
add = lambda a, b: a + b
result = add(3, 5)
print(result)

#lambda map()
numbers = [1, 2, 3, 4]
double = lambda a : a * 2
result = map(double, numbers)#map in this case is used to double the list of numbers given
print(list(result))#outputs it as a list

#lambda filter()
num = [1, 2, 3, 4, 5, 6]
result = filter(lambda n : n % 2 == 0, num)
print(list(result))

#lambda reduce()
#to use reduce we import it first, done above
expenses = [
    ('dinner', 80),
    ('car repair', 120)
]
sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)