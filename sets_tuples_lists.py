# collection = single "variable" used to store multiple values 
#lists = [] ordered and changable. duplicates ok 
# set = {} unordered and immutable, but add\remove ok, no duplicates 
# tunple = ( ordere and unchanegable. duplicates ok. FASTER

fruit = ["apple", "orange ", "banana", "coconut","kiwi","nuts"]
len(fruit)
print(len)
print(fruit[0])
print(fruit[0:3]) 
print(fruit[::2]) #skips 2 after the second one 
print(fruit[::-1]) #prints the list backwards 
#print(dir(fruit))# dir basically gives you all the atributes for the list 
#print(help(fruit))#gives you helpful documentation 
print(len(fruit))#gives you the lenght of your list 
print("apple" in fruit) # prints so chekc if the string is in the list by saying true or false 
#fruit[1]="kiwi" #it changes the values kiwi second to last now makes it the value of 1 
#fruit.append("kiwi") #adds the element to the end of the list
#print(fruit)
#fruit.remove("banna") #removes the element 

# fruit.insert(0, "apple")# inputs an element at a certain value 

# fruit.sort()
# fruit.reverse()
# fruit.clear()#removes evrything 
print(fruit.index("apple")) #finds the index of the element 

print(fruit)
#for x in fruit:
    #print(x)




cars = ["Ford", "volvo", "BMW"]

cars.insert(0, "honda") 
cars.append("Mercedes")
cars.append("Maserati")
cars.append("porche")

print(cars)

print("The cars on the list are:", cars)
print(f"The cars in the list are: {cars}")
cars[-1] = "ausitn martin"
print(f"The cars in this list are: {cars}")
cars[3]="chevy"
print(f"The cars in this list are: {cars}")
cars.insert(0, "lexus")
print(f"The cars in this list are: {cars}")
cars.remove("chevy")
print(f"the cars in this list are: {cars}")
print("ford" in cars)

# for car in cars:
#     requestcar= input("Enter a car: ")
#     cars.append(requestcar)
#     print(f'The cars in the list are: {cars}')
#     if len(cars) > 10:
#         print("You have rached the maximum number of cars")
#         break

friends = ["Ignacio"]

# for friend in friends:
#     requestmorefriedns=input("Enter four new friedns:")
#     friends.append(requestmorefriedns)
#     print(f'The friedns on this list are: {friends}')
#     if len(friends) > 5        
#     break


#Sets are unordered and unindexed 
#they are defied using curly brackets 
#they do not allow dupicates 
fruits = {"apple", "bananna", "mango", "cherry", "watermelon"}


#print(dir(fruits))#methods that can be used with sets 
#print(help(fruits))#documentation/methods that can be used with sets 
#print(len(fruits))#number of elements in the set 
#print("volvo" in fruits)#check if an element is in the set 
print(fruits.add("orange"))
print(fruits)
print(fruits.add("kiwi"))
print(fruits)
#print(fruits.update{["orange", "kiwi", "pineapple"]})
#add multiple elements to the set 
#print(fruits.remove("bannana"))
print(fruits)
print(fruits.pop())
print(fruits)
print(fruits.clear())
print(fruits)
#when do we want to use sets?
#sets are useful when you want to store a collection of items that should not be changed
#and you do not care about the order of the items 
#example: a collection of unique items 
social_security_numbers = {123456789, 987654321, 123456789}
#remove the last elemet in this set 
#add another social security number 
print(social_security_numbers)
print(social_security_numbers.add(345678901))
print(social_security_numbers)

#tuples are immtable and are defined using parenthesis 
#create a tuple called my_tuple with the following values
example_tuple = (1,2,3,4,5,6,7,8,9,10,10)
print(example_tuple)
print(example_tuple.count(2))#count the number of times\
#the value appears 2 in the tuple
# print(dir(example_tuple))
# print(help(example_tuple))

# print(len(example_tuple))
# print(2 in example_tuple)

# print(example_tuple.index(2))

# lymeric= "peter pipe picked a peck of pickeled peppers"
# lymeric=tuple(lymeric.split())
# print(lymeric)

# print(lymeric.count("pick"))

#loops with tuples
for item in example_tuple:
    print(item)

#dictionary

#Dictionaries are unordered, changeable and indexed 
#they are defined using cury brackets 
#they have keys and brackets 
# a collections {key:value} pairs, no duplicates 
#keys are unique 
#values can be of any data type 
capitals= {"Kenya":"nairobi",
           "Uganda":"kampala",
           "Tanzania":"Dodoma",
           "Rwanda":"Kigali",
           "china":"beijing",
           "USA":"Washington DC"}
# print(capitals)
# print(dir(capitals))
# print(help(capitals))
# print(len(capitals))
print(capitals["Kenya"])
print(capitals.get("Kenya"))
capitals["South africa"] = "pretoria"
print(capitals)
capitals.update({"Nigeria":"Abruja"})
print(capitals)
capitals.update({"Colombia":"Venezuela"})
capitals.update({"Mexico":"guatemala"})
print(capitals)

# capitals.pop("guatemala")
# print(capitals)

for key in capitals:
    print(f"these are the {key}")


#for value in capitals.values():
    #print(value)

item_all = capitals.items()

for key, value in item_all:
    print(f"{key} is the capital of {value}")