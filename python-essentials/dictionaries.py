#Dictionaries
laptop = {"brand": "Hp", "type": "Elite Book", "Keyboard": "Backlit", "screen size": "14inch", "RAM": "8gb"}
print(laptop['brand'])#prints the value of the key brand

laptop["type"] = "Note Pad"#changes the type from elite to note
print(laptop.get("type"))#outputs the type key
print(laptop)#outputs the whole dictionary
print("\n")

print(laptop.pop("type"))#removes the specific key in this case type
print(laptop)#prints after it has been removed
print("\n")

print(laptop.popitem())#prints the last item in the dictand removes it
print(laptop)#prints the whole dict after removing the last thing
print("\n")

print("RAM"in laptop)#checks is a specific key is in the dict
print(laptop.keys())#prints all the keys in that dictionary
print(laptop.values())#prints all values in the dictionary
print(list(laptop.items()))#prints all the items in the dict and convert it into a list
print("\n")

laptop["Hard drive"] = "512ssd"#adds a new item to the dict
print(laptop)
laptopCopy = laptop.copy()#copies the dict
print(laptop)
print("\n")

#SETS
names1 = {"Cindy", "Jeby", "Red"}
names2 = {"Cindy", "Monday", "Blue"}

intersect = names1 & names2
print(intersect)#prints what the 2 sets have in comon
mod = names1 | names2
print(mod)#prints both sets combined
print("\n")

set1 = {"water", "bender"}
set2 = {"water"}
sets = set1 - set2 
print(sets)#prints the difference

#checks if a set is a superset or a subset
sets = set1 > set2
print(sets)
sets = set1 < set2
print(sets)