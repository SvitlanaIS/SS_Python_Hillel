class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def __str__(self):
         return f"{self.first_name} {self.last_name}, {self.gender}, {self.age}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
         return super().__str__()+ f", {self.record_book}"

class GroupLimitException(Exception):
    def __init__(self, message="Неможливо додати більше 10 студентів до групи."):
        self.message = message
        super().__init__(self.message)

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
            print(f"Студент {student.last_name} доданий до групи {self.number}")
        else:
             raise GroupLimitException()

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
            print(f"Студент {last_name} видалений із групи {self.number}")
        else:
            print(f"Студент {last_name} не знайдено у групі {self.number}")

    def find_student(self, last_name):
        return next((student for student in self.group if student.last_name == last_name), None)

    def __str__(self):
        all_students = "; ".join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 31, 'Oliver', 'Smith', 'AN146')
st4 = Student('Female', 26, 'Olivia', 'Johnson', 'AN148')
st5 = Student('Male', 33, 'Harry:', 'Williams', 'AN149')
st6 = Student('Female', 28, 'Emily', 'Jones', 'AN141')
st7 = Student('Male', 35, 'Charlie', 'Brown', 'AN143')
st8 = Student('Female', 29, 'Isabella', 'Davis', 'AN147')
st9 = Student('Male', 36, 'Thomas', 'Miller', 'AN144')
st10 = Student('Female', 27, 'Charlotte', 'Wilson', 'AN140')
st11 = Student('Female', 25, 'Abigail', 'Davies', 'AN150')

gr = Group('PD1')

try:
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
    gr.add_student(st11)
except Exception as e:
    print(f"Error: {e}")

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!