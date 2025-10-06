class Employee:
    def __init__(self, position, salary, experience):
        self.position = position
        self.salary = salary
        self.experience = experience
    
    def get_job_info(self):
        return f"{self.position}, {self.experience} роки досвіду, зарплатня: {self.salary} uah"
