class Student:
    ...
    # attributes or instance variables: name, students

def main():
    # get_student() returns a tuple
    student = get_student() 
    print(f"{student.name} is from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()