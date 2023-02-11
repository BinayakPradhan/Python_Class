# # # class Sagarmatha:
# # #     def __init__(self, no_of_departments = 2, no_of_students = 500):
# # #         self.affiliation = "TU"
# # #         self.no_of_departments =  no_of_departments
# # #         self.location = "Sanepa"
# # #         self.no_of_students = no_of_students
# # #         self.no_of_faculty = (no_of_students/100)
    

# # #     def canteen_profit(self):
# # #         return self.no_of_students * 0.1 * 10

# # # class SagarmathaTechnology(Sagarmatha):
# # #     super().__init__(self, no_of_departments = 2, no_of_students = 500):
# # #         self.affiliation = "TU"
# # #         self.no_of_departments =  no_of_departments
# # #         self.location = "Sanepa"
# # #         self.no_of_students = no_of_students
# # #         self.no_of_faculty = (no_of_students/100)
    

# # #     def canteen_loss(self):
# # #         return self.no_of_students * 0.5 * 10


# #super ko use
# # class Animal:
# #     def __init__(self, name):
# #         self.name = name
        
# #     def make_sound(self):
# #         print("Some animal sound")
       
        
# # class Dog(Animal):
# #     def make_sound(self):
# #         super().make_sound()
# #         print("Woof!")
    
# # dog = Dog("Max")
# # print(dog.name)
# # dog.make_sound()


# #access specifiers
# class Car:
#     def __init__(self, make, model, year):
#         self.__make = make
#         self.__model = model
#         self._year = year
        
#     def get_make(self):
#         return self.__make
    
#     def get_model(self):
#         return self.__model
    
#     def get_year(self):
#         #protected
#         return self._year
    
#     def set_make(self, make):
#         self.__make = make
        
#     def set_model(self, model):
#         self.__model = model
        
#     def set_year(self, year):
#         self._year = year
        
# car = Car("Toyota", "Camry", 2022)
# print("Make:", car.get_make())
# print("Model:", car.get_model())
# car.set_year(2021)
# print("Year:", car.get_year())

# In this example, we have a class Car that represents a car object. The class has three attributes: __make, __model, and __year, which store the make, model, and year of the car, respectively.

# Access to the attributes is controlled through methods get_make, get_model, and get_year, which return the values of the corresponding attributes. The attributes can also be modified through methods set_make, set_model, and set_year.

# Notice that the attributes have names that start with double underscores, which makes them private. This means that they cannot be directly accessed from outside the class. Instead, they can only be accessed through the methods.

# This demonstrates how encapsulation allows you to hide the implementation details of an object and control access to its attributes, making it easier to maintain and change the implementation over time.