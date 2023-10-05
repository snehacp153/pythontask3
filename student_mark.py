class Student:
    def get_data(self):
        self.rollno = int(input("enter the rollno:"))
        self.name = input("enter the name:")

    def print_data(self):
        print("the rollno of student is:",self.rollno)
        print("the name of student is:",self.name)



class Mark(Student):
    def input_data(self):
        super().get_data()
        self.physics =int(input("Enter Physics Marks : "))
        self.chemistry = int(input("Enter Chemistry Marks : "))
        self.maths = int(input("Enter Maths Marks : "))
        self.english = int(input("Enter english Marks : "))
        self.hindi = int(input("Enter hindi Marks : "))
        self.total = self.physics + self.chemistry + self.maths + self.english + self.hindi 

    def out_data(self):
        super().print_data()
        print("mark for english is ",self.english,"for physics is",self.physics," for chemistry is",self.chemistry," for maths is",self.maths," for hindi is",self.hindi, "and total mark is" ,self.total)
        

obj = Mark()
obj.input_data()
obj.out_data()