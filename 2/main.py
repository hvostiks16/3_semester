from student import Student
from teacher import Teacher

student1 = Student(1, "Oleksandra", "Khvostova", "Andriivna",
                   "0977999305", "hvosto28@gmail.com", "16.05.2007",
                   "Lviv", "Frankivskyi", "Lukasha", "5",
                   "-", "-", "11a")

student2 = Student(2, "Violetta", "Kalabska", "Oleksiivna",
                   "0965749023", "violka@gmail.com", "05.06.2007",
                   "Lviv", "Frankivskyi", "Lukasha", "5",
                   "-", "-", "11a")

teacher1 = Teacher(1, "Natalia", "Sofiichuk", "Dmytrivna",
                   "0965105834", "pryvitov_school@ukr.net",
                   "teacher", 15000, 43)

#______________________________________________________________
print("ІНФОРМАЦІЯ ПРО СТУДЕНТА")
print(Student.is_valid_name(student1.name))
print(f"ПІБ: {student1.get_full_name()}")
print(f"Адреса: {student1.get_address()}")
print(f"E-mail до внесення змін: {student1.email}")
student1.update_email("hvosto28@ukr.net")
print(f"E-mail після внесення змін: {student1.email}")
print()

print("ІНФОРМАЦІЯ ПРО ВЧИТЕЛЯ")
print(teacher1.get_full_info())
print(f"Phone number до внесення змін: {teacher1.get_phone_number()}")
teacher1.update_phone_number("0977999307")
print(f"Phone number після внесення змін: {teacher1.get_phone_number()}")
print()

print("СПИСОК УЧАСНИКІВ НАВЧАЛЬНОГО ПРОЦЕСУ")
people = [student1, student2, teacher1]
for person in people:
    print(f"☺ {person.get_full_name()}: {person.get_status()}")
print()

print("ЗАПИС УЧНІВ ДО КЛАСУ")
student1.enroll_student()
student2.enroll_student()
print()

print("НАДСИЛАННЯ ПОВІДОМЛЕНЬ БАТЬКАМ")
teacher1.send_message_to_parent(student1, "Нагадуємо про збори 11а класу в середу о 18:00.")

teacher1.send_message_to_parent(student2, "Дорогі батьки, чекаємо вас на розмову з класним керівником 23.10 о 17:00")
