# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]
# 1. lists comprehensions example
# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

# 2. filter function
# def is_Gryffindor(student):
#     return student["house"] == "Gryffindor"
# gryffindors = filter(is_Gryffindor, students)

# for gryffindor in sorted(gryffindors, key= lambda gryffindor: gryffindor["name"]):
#     print(gryffindor["name"])

# 3. dictionary comprehension example

students = ["Harry", "Hermione", "Ron"]
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)