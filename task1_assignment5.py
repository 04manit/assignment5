dict1 = {
    "Alice": 72,
    "Albert": 77
}

name = input("Enter the student's name: ")
if dict1.get(name) == None:
    print("Student not found.")
else:
    print(name + "'s marks:", dict1.get(name))