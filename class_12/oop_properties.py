class Sagarmatha:
    def __init__(self, no_of_departments = 2, no_of_students = 500):
        self.affiliation = "TU"
        self.no_of_departments =  no_of_departments
        self.location = "Sanepa"
        self.no_of_students = no_of_students
        self.no_of_faculty = (no_of_students/100)
    

    def canteen_profit(self):
        return self.no_of_students * 0.1 * 10

class SagarmathaTechnology(Sagarmatha):
    super().__init__(self, no_of_departments = 2, no_of_students = 500):
        self.affiliation = "TU"
        self.no_of_departments =  no_of_departments
        self.location = "Sanepa"
        self.no_of_students = no_of_students
        self.no_of_faculty = (no_of_students/100)
    

    def canteen_loss(self):
        return self.no_of_students * 0.5 * 10