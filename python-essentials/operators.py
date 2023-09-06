#Assign Operator
money = 20 #we use the eqaul sign to assign the value 20 to age

#arthmitic operators
age = 8
age *= 8
print(age)

#complex numbers
num1 = 2+3j
num2 = complex(2, 3)
print(num2.real, num2.imag)

#enums
from enum import Enum
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
print(State.ACTIVE.value)#prints 1
print(State.INACTIVE.value)#prints 0
print(list(State))
print(len(State))