import sys

class Student:
    def __init__(self,name,age,lastname,salary):
        self.name = name
        self.age = age
        self.lastname = lastname
        self.salary = salary

obj_student = Student("pallab mahapatra",30,'mahapatra',60000)

print(id(obj_student))

print(id(obj_student.name))

print(id(obj_student.age))

print(id(obj_student.lastname))

print(id(obj_student.salary))

print(sys.getsizeof(obj_student))