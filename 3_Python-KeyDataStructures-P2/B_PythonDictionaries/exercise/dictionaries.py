#Initialise a dictionary
my_dict = {
    "name": "Alice",
    "age": 26,
    "city": "New York"
    }

#Access an element in the dictionary
print(my_dict["name"])

#Update an element in a dictionary
my_dict["age"] = 27
print(my_dict)

#Add a new key-element pair
my_dict["email"] = "alice@example.co.uk"
print(my_dict)

#Remove key-value pair
my_dict.pop("city")
del my_dict["name"]
print(my_dict)

#Iterate through the dictionary
for x in my_dict:
    print(x)
