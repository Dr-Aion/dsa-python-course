import csv
students = [] 

with open("students.csv") as file:
    # approach 1
    # for line in file:
    #     # you can unpack the sequence
    #     name, house = line.rstrip().split(",")
    #     # print(f"{name} is in {house}")
    #     # students.append(f"{name} is in {house}")
    #     student = {}
    #     student["name"] = name
    #     student["house"] = house
    #     print(student)
    #     students.append(student)

    # approach 2 using csv library
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name": name, "house": house})        

# def get_name(student):
#     return student['name']

# def get_house(student):
#     return student['house']

for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")
