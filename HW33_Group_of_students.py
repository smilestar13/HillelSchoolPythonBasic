class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.gender}: {self.first_name} {self.last_name} {self.age} years old'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.gender}: {self.first_name} {self.last_name} {self.age} years old (#{self.record_book})'


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        res = self.find_student(last_name)
        for st in self.group:
            if res == st:
                self.group.remove(st)
                break
        return self.group

    def find_student(self, last_name):
        for st in self.group:
            if last_name in str(st):
                return st

    def __str__(self):
        all_students = ''
        for st in self.group:
            all_students += f'\n{st}'
        return f'Number:{self.number}\n {all_students}'


st1 = Student('Male', 27, 'Ivan', 'Helicopter', 'AN143')
st2 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st3 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st4 = Student('Female', 42, 'Liza', 'Vasylenko', 'AN159')


gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
# print(gr)

print(gr.find_student('Jobs'))
print(gr.find_student('Jobs2'))  # None

gr.delete_student('Taylor')
print(gr) # Minus one student