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

for car in cars:
    requestcar= input("Enter a car: ")
    cars.append(requestcar)
    print(f'The cars in the list are: {cars}')
    if len(cars) > 10:
        print("You have rached the maximum number of cars")
        break