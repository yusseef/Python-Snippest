#Dictionary: Key-value pairs, Unordered, Mutable

Dict = {"name":"Yussef", "age":22, "city":"Alexandria"} #Declaring a dictionary
Dict = dict(name="Mary", age=27, city="Cairo") #Declaring by a dict function
Value = Dict["name"] #To access a value by a key
Dict["email"] = "Yussef@email.com" #Add new item
Dict["email"]  = "email@email.com" #Edit email item 
del Dict["email"] #Delete item
Dict.pop("email") #Delete item
Dict.popitem() #Delete last item

for key in Dict.keys():
    print(key) #To print all the keys

for value in Dict.values():
    print(value) #To print all the values

for key, value in Dict.items():
    print(key, value) #Print both keys and values

Dict_cpy = Dict.copy() #To copy the dictionary

Dict_1 = {"name":"yussef", "age":22, "email":"email@email.com"}
Dict_2 = dict(name="mary", age=20, city="Cairo")
Dict_1.update(Dict_2) #To merge to dictionaries
print(Dict_1)

{key:value for (key,value) in Dict.items} #Dictionary comprehinsion
{key:value*2 for (key,value) in Dict.items} #Dictionary comprehinsion with values * 2

