#While loop

count = 0
while count < 10:#the loop repeats until count is greater than 10
    print("The condition is True")
    count = count + 1
print("Loop ends here at False")#when the count is greater than 10 it prints this messege.

#For loop
items = [1, 2, 3, 4]
for item in items:
    print(item)

#For loop example 2
for item in range(10):
    print(item)

#For loop example 3
colors = ["black", "blue", "pink", "purple"]
for color in enumerate(colors):
    print(color)#this prints index of the items against the items in the list

#For loop example 4(continue)
numbers = [3, 4, 5, 6, 7]
for number in numbers:
    if number == 5:
        continue
    print(number)#it will skip 5 and continue with the rest

#For loop example 5
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 4:
        break#it will stop at 3
    print(num)