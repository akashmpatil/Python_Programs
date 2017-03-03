class Employee:
            #def__init__(self)
            #      print("consttructor with zero para")
            def __init__(self,name,designation):
                  self.name=name
                  self.designation=designation
            def display(self):
                  print("name",self.name)
                  print("designation",self.designation)
emp2=Employee("akash","Consultant")
emp2.display()