from person import Person

class Student(Person):
    def __init__(self, id, name, surname, patronymic, 
                 phone_number, email, date_of_birth, 
                 city, neighborhood, street, building, 
                 apartment, privilege, id_class):
        super().__init__(id, name, surname, patronymic, phone_number, email)
        self.date_of_birth = date_of_birth
        self.city = city
        self.neighborhood = neighborhood
        self.street = street
        self.building = building
        self.apartment = apartment
        self.privilege = privilege
        self.id_class = id_class
    
    def get_address(self):
        return f"{self.city}, {self.neighborhood}, {self.street}, {self.building}, {self.apartment}"

    def get_status(self):
        return "student"
    
    def enroll_student(self):
        print(f"► {self.get_full_name()} записано в {self.id_class} клас")
