#!/usr/bin/python3
import pickle

# Define a Python object (dictionary)
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Serialize the object to a binary file
with open("person.pickle", "wb") as f:
    pickle.dump(person, f)

# Read serialized file
with open("person.pickle", "rb") as f:
    serialized_data = f.read()

# Deserialize the object from the binary file
with open("person.pickle", "rb") as f:
    loaded_person = pickle.load(f)

# print the content of the serialized file
print("serialized_data =", serialized_data)

# Print the deserialized object
print("loaded_person =", loaded_person)

