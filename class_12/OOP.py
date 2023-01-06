# #Example 1

# # class Sagarmatha:
# #     def __init__(self):             #__init__ is a constructor esle garda esko bhitra ko print huncha
# #         print("Constructor has been created.")
# #     def home(self):                 #home chai hamro normal function ho ani esko access garna self is mandatory
# #         print("Home Sweet Home!")
# #     def __del__(self):              #__del__ is a destructor ani esko bhitra ko print huncha end ma
# #         print("Destructor has been created.")
# # #Call using Class
# #     def classcalling():             #classcalling hamro normal function ho
# #         print("Self use nagari access gareko")
# # Sagarmatha.classcalling()

# # #Call using Object
# # sg = Sagarmatha()               #sg is an object of class Sagarmatha
# # sg.home()                       #object ko function access gareko


# #Example 2

# class BCT:
#     def __init__(self,name,age,rollno,subject):
#         self.name = name
#         self.age = age
#         self.rollno = rollno
#         self.subject = subject
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.rollno)
#         print(self.subject)
# #value sent in an object
#     def jpt(self,address):
#         print(f"My name is {self.name} and I live in {address}")

# st1 = BCT("Sworrrnima",16,46,"Maths")
# st2 = BCT("Binayak",21,16,"Python")

# st1.jpt("Dhumbarahi")
# st1.display()
# st2.display()

class Visualization:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def home(self):
        print(self.name, self.age)

viz = Visualization('Shelby',35)
viz.home()

