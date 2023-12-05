# The class can be defined as a collection of objects. It is a logical entity that has some specific attributes and methods.
# The object is an entity that has state and behavior. It may be any real-world object like the mouse, keyboard, chair, table, pen, etc.

class car:  
    def __init__(self,modelname, year):  
        self.modelname = modelname  
        self.year = year  
    def display(self):  
        print(self.modelname,self.year)  
  
c1 = car("Toyota", 2016)  
c1.display()  

# Output :

# Toyota 2016