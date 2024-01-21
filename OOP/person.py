class Person:
    # instance variables: name, weight, height
    def __init__(self, name = "", weight = 1, height = 1):
        self.name = name
        self.weight = weight
        self.height = height
    
    def __str__(self):
        return f"{self.name} is a person whose weight is {self.weight} and height {self.height}"
    
    def calculate_bmi(self):
        return self.weight/(self.height * self.height)

Aiganym = Person("Aiganym", 68, 179)
noName = Person("", 78, 190)
print(noName)
print(noName.calculate_bmi())

print(Aiganym)

