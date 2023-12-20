# # writing to a file
# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# reading from a file
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")