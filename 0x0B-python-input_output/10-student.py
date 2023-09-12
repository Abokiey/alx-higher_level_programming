#!/usr/bin/python3

"""class student"""


class Student:
    """instantiation"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves the dictionary representation"""
        if attrs is None:
            return (self.__dict__)
        else:
            dictionary = {}
            for at in attrs:
                if at in self.__dict__.keys():
                    dictionary[at] = self.__dict__[at]
            return (dictionary)

if __name__ == "__main__":
    

    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
