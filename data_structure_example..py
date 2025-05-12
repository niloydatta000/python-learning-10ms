# Hypothetical Python Programmer Group

'''
Combined Data Structure Manipulation: List[], Dictionary{}, Tuple()

File name: DataStructureExample.py
'''

# Start with Declaring a Variable

users = [
    {
        "name" : "Niloy",
        "age" : 25,
        "e-mail" : "niloydatta000@gmail.com",
        "interests" : ["Football", "Cricket"],
        "location" : ("Dhaka", "Bangladesh")
    },
    {
        "name" : "John",
        "age" : 23,
        "e-mail" : "john@example.com",
        "interests" : ["Football", "Badminton"],
        "location" : ("London", "UK")
    },
    {
        "name" : "Harry",
        "age" : 24,
        "e-mail" : "harry@example.com",
        "interests" : ["Soccer", "Swimming"],
        "location" : ("New York", "USA")
    },
    {
        "name" : "Alice",
        "age" : 20,
        "e-mail" : "alice@example.com",
        "interests" : ["Cricket"],
        "location" : ("Sydney", "Australia")
    },
    {
        "name" : "Jing",
        "age" : 21,
        "e-mail" : "jing@example.com",
        "interests" : ["Football", "Hockey"],
        "location" : ("Beijing", "China")
    }
]

# Print the details of each programmer
print("Details of the programmers:\n")
# Loop through the list of users
for programmer in users:
    print(" ")
    print(f"Name : {programmer['name']}")
    print(f"Age : {programmer['age']}")
    print(f"Country : {programmer['location'][1]}")
    print(f"City : {programmer['location'][0]}")
    print(f"E-mail : {programmer['e-mail']}")
    print("Interests :", end=" ")
    if len(programmer['interests']) == 1:
        print(programmer['interests'][0] + "\n")
    for interest in programmer['interests'][:-1]:
        print(interest, end=", ")
        print(programmer['interests'][-1] + "\n")

