# Dictionary is a collection by association of keys and values
classes = {"CA100":"Computer Literacy", "IS280" :"Networking", "IS220":"Programming", 
           "IS230": "Database"}

# Traverse a dictionary using the key
for key in classes:
    print(key,":",classes[key])

print("-"*30)
# Traverse a dictionary using the key and value
for (key, value) in classes.items():
    print(key,":",value)


print("-"*30)
# Traverse a dictionary using the value only
for (value) in classes.values():
    print(value)

# Convert the keys to list and then traverse
print("-"*30)
courseCodes = list(classes.keys())
courseCodes.sort()
for courseCode in courseCodes:
    print(courseCode)
