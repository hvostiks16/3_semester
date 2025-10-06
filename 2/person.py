class Person:
    def __init__(self, id, name, surname, patronymic, phone_number, email):
        self.__id = id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.__phone_number = phone_number
        self.email = email

    def get_full_name(self):
        return f"{self.name} {self.patronymic} {self.surname}"
    
    def get_phone_number(self):
        return self.__phone_number
    
    def update_phone_number(self, new_number):
        self.__phone_number = new_number
    
    def update_email(self, new_email):
        self.email = new_email
    
    @staticmethod
    def is_valid_name(name):
        return name.isalpha()

    def get_status(self):
        return "person"

