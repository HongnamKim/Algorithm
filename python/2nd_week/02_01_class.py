class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("I'm " + self.name)

person_1 = Person('aa')
person_2 = Person('bb')

print(person_1.talk())
print(person_2.talk())