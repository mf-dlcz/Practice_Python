#       Student

class Student:
    def __init__(self, name: str, color: str, quarter: int, hobby: str):
        self.name = name
        self.color = color
        self.quarter = quarter
        self.hobby = hobby

    def print_hobby(self):
        self.hobby
        return f'{self.name} loves {self.hobby}'

    def print_all_details(self):
        self.name
        self.color
        self.quarter
        self.hobby
        return f'Name: {self.name} \nColor: {self.color} \nQuarter: {self.quarter} \nHobby: {self.hobby}'


student1 = Student('Maria', 'grey', 1, 'hiking')
print(student1.print_hobby())
print(student1.print_all_details())