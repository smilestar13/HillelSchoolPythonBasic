from HW33_Class__Student import *
from HW33_Class__Group import *


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
print(gr.find_student('Jobs'))  # 'Steve Jobs'
print(gr.find_student('Jobs2'))  # None

gr.delete_student('Taylor')
print(gr)  # Only one student
