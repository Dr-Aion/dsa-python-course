import csv

students = [] 

with open("students.csv") as file:
    for line in file:
        man, home = line.rstrip().split(",")
        student = {"names": name, "home":home}
        students.append(student)
