class Person:
    def __init__(self,name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person class created.")
    
    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    pass

class Teacher(Person):
    pass


p1 = Person("ibrahim","kus",37)
p1.intro()

s1 = Student("n1","n1",11)
s1.intro()
t1 = Teacher("t1","t1",22)
t1.intro()