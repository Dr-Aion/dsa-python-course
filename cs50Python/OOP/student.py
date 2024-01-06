class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} is from {self.house}"
    # attributes or instance variables: name, students

def main():
    # get_student() returns a tuple
    student = get_student() 
    print(student)

def get_student():
    name = input("Name: ").strip()
    house = input("House: ").strip()
    return Student(name, house)

if __name__ == "__main__":
    main()