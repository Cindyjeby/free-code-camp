#lists
cars = ["Bmw", "Audi", "Range Rover", "Jeep"]
print("toyota" in cars) # in is used to check the list
print("Bmw" in cars)

print(cars[3]) # references an item in the list using its index

cars[0] = "Toyota"#changes the item at  the specified index to the new item given
print(cars)#lists the whole list
print("\n")

cars.append("Bentley")#adds items to a list
print(cars)#lists the whole list
print("\n")

cars.extend(["Rolls Royce", "Ferrary", "Ford"])#adds multiple items to a list or combine 2 list together at the end
print(cars)#lists the whole list
print("\n")

cars.remove("Jeep")#removes an item
print(cars)#lists the whole list
print("\n")

print(cars.pop())#removes the last item on the list
print(cars)#lists the whole list
print("\n")

cars.insert(2, "Jeep")#inserts item at specified part of the list
print(cars)#lists the whole list
print("\n")

cars[1:1] = ["Bmw","Mercedes", "bmw", "chevrolet", "honda", "hummer"]#inserts lists of items at specifed position
print(cars)
print("\n")

carscopy = cars [:]#copies original before sort
print("\n")
cars.sort()#sorts list in alphabetical order.sorts upercase first then lowercase
print(cars)
print("\n")

cars.sort(key=str.lower)#sorts alphabeticaly both uper and lowecase
print(cars)
print("\n")
print(carscopy)

print(len(cars))#gives length
print("\n")

#Tuples
brands = ("Toshiba", "Hp", "Sony", "Dell", "Lenovo", "Acer")
print(brands.index("Toshiba")) #prints index of the item 

#new tuple
newBrands = brands + ("Scorpion", "Marvo", "Hikvision")
print(newBrands)
print("\n")