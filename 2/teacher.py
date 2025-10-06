from person import Person
from employee import Employee

class Teacher(Person, Employee):
    def __init__(self, id, name, surname, patronymic, phone_number, email,
                 position, salary, experience):
        Person.__init__(self, id, name, surname, patronymic, phone_number, email)
        Employee.__init__(self, position, salary, experience)

    def get_full_info(self):
        return f"{self.get_full_name()}: {self.get_job_info()}"

    def get_status(self):
        return f"{self.position}"
    
    def send_message_to_parent(self, student, message):
        print(f"Повідомлення для батьків {student.get_full_name()}: {message}")