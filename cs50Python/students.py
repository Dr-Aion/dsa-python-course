import csv

students = [] 

with open("students.csv") as file:
    for line in file:
        # you can unpack the sequence
        name, house = line.rstrip().split(",")
        # print(f"{name} is in {house}")
        # students.append(f"{name} is in {house}")
        student = {}
        student["name"] = name
        student["house"] = house
        print(student)
        students.append(student)

def get_name(student):
    return student['name']

def get_house(student):
    return student['house']

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")
