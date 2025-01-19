class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person sınıfı türetildi.")

    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person): #child class
    def __init__(self, name, surname, age, number):
        #Person.__init__(self,name,surname,age) #alternative super()....
        super().__init__(name, surname, age)
        self.number = number
        print("student class türetildi.")    

    def study(self):
        print(f"{self.name} ders çalışıyor.")

    def intro(self):
        print(self.name, self.surname, self.age, self.number)

class Teacher(Person): #child class
    def __init__(self, name, surname, age, branch):
            super().__init__(name, surname, age)
            self.branch = branch
            print("teacher class türetildi.") 

    def teach(self):
         print(f"{self.name} {self.branch} dersi anlatıyor.") 

p1 = Person("ibrahim","kus", 40)
p1.intro()

s1 = Student("cagri","kus",7, 105)
s1.intro()
# s1.study()
# print(s1.number)

t1 = Teacher("Ali","Korkmaz",35,"math")
t1.intro()
# print(t1.branch)
# t1.teach()