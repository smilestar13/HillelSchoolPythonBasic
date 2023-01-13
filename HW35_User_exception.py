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
        if len(self.group) == 10:
            raise UserException('\nДостигнут максимум студентов!!!\n')
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        res = self.find_student(last_name)
        self.group.discard(res)

    def find_student(self, last_name):
        for st in self.group:
            if last_name in str(st):
                return st

    def __str__(self):
        all_students = ''
        for st in self.group:
            all_students += f'\n{st}'
        return f'Number:{self.number}\n {all_students}'


class UserException(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message


# Основной костяк группы 1
st1 = Student('Male', 27, 'Ivan', 'Helicopter', 'AN143')
st2 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st3 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st4 = Student('Female', 42, 'Liza', 'Vasylenko', 'AN159')
st5 = Student('Male', 22, 'Antony', 'Ivanov', 'AN151')
st6 = Student('Male', 18, 'John', 'Stepanov', 'AN152')
st7 = Student('Female', 32, 'Ann', 'Kryak', 'AN153')
st8 = Student('Female', 33, 'Dasha', 'Great', 'AN154')
st9 = Student('Male', 41, 'Stepan', 'Jonhsonuk', 'AN155')
st10 = Student('Male', 27, 'Anatoly', 'Stepanchuk', 'AN156')

# Дополнительный студент вне диапазона группы
st11 = Student('Female', 11, 'Victoria', 'Amare', 'AN161')

# Добавляем основной костяк в группу
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
print(f'Группа студентов в начале: \n{gr}')

# Пробуем добавить студента вне диапазона количества группы. Вызов ошибки сделал через \n чтобы бросалась в глаза сразу
try:
    gr.add_student(st11)  # ValueError
except UserException as e:
    print(e.message)  # Достигнут максимум

# Поиск студентов по фамилиям
print(gr.find_student('Jobs'))
print(gr.find_student('Jobs2'))  # None

# Исключение студента из группы
gr.delete_student('Taylor')

# Пробуем еще раз добавить новенького после исключения плохиша
try:
    gr.add_student(st11)  # ValueError
except UserException as e:
    print(e.message)  # Достигнут максимум

# Выводим финальную группу студентов
print(f'\nФинальная группа: \n{gr}')
