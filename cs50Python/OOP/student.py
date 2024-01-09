class Student:
    # attributes or instance variables: name, students
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self._name} is from {self._house}"
    
    # house is a property of our class, 
    # with functions via which a user attempts to set our class attribute. 
    # _house is that class attribute itself. 
    # The leading underscore, _, indicates to users they need not (and indeed, shouldn’t!) 
    # modify this value directly. _house should only be set through the house setter. 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    @classmethod
    def get(cls):
        name = input("Name: ").strip()
        house = input("House: ").strip()
        return cls(name, house)

def main():
    # get_student() returns a tuple
    student = Student.get() 
    print(student)


if __name__ == "__main__":
    main()