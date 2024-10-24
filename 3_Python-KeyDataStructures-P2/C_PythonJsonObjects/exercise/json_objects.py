import json

#Define a JSON string
json_string = '{"name": "Alice", "age": 25, "city": "New York"}'

#Parse the JSON data
data = json.loads(json_string)
print(data)
print(data["name"])
data["age"] = 26
print(data)

#Convert the python dictionary back to JSON data
json_data = json.dumps(data)
print(json_data)
