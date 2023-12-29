import csv
name = input("What's your name? ")
home = input("What's your home? ")

with open("students1.csv", "a") as file:
    # approach 1 using csv library writer() method
    # writer = csv.writer(file)
    # writer.writerow([name, home])

    #approch 2 using csv library DictWriter() method
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow({"name": name, "home": home})
    

