from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_year_of_birth(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_of_legal_age(age):
        return age >= 18


person1 = Person('John', 26)
person2 = Person.from_year_of_birth('Math', 2000)

print(person1.age)
print(person2.age)
print(Person.is_of_legal_age(17))
