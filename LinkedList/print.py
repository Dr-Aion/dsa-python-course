class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person {self.name} - {self.age}"
    
newPerson = Person("Aiganym", 32)
print(newPerson)