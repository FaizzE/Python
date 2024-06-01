fruits = ["apple", "banana","kiwi","mango"]
newFrruits=[]
for x in  fruits:
       if "a" in x:
           newFrruits.append(x)
           
print(newFrruits)

# Second MEthod
fruits = ["apple", "banana","kiwi","mango"]
newFrruits=[x for x in fruits if "a" in x]

print(newFrruits)
