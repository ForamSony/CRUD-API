# from abc import ABC#, abstractmethod, abstractclassmethod

# class Shape(ABC):
#   #  @abstractmethod
#     def area(self):
#         pass

#   #  @abstractmethod
#     def edge(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def vertices(self):
#         print("This is vertices")

#     def area(self):
#         return 3.14*self.radius
    
#     def edge(self):
#         return 3.14

# c = Circle(5)
# print(c.vertices())
# print(c.area())
# print(c.edge())



from abc import ABC, abstractmethod

class Shape(ABC): # abstract class wich have atleast 1 abc method

    @abstractmethod # after @ is called decorator
    def area(self): # abc method : all subclass must have this method
        pass

    def display(self): # concrete / normal method 
        print("calling from super")

class Circle(Shape):

    def __init__(self,r):
        self.r = r 

    def area(self):
        return 3.14*self.r*self.r
    def Circumference(self):
        return 3.14*2*self.r

c = Circle(int(input("Enter redius of Circle:")))  
print("Area of Circle:",c.area() ) 
print("Circumference of Circle:",c.Circumference())

class triangle(Shape):

    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return (self.base*self.height)/2 
    
t = triangle(int(input("Enter base of Triangle:")),int(input("Enter height of Tringle:")))
print("Area of Tringle:",t.area())

class rectangle(Shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    
re = rectangle(int(input("Enter length of Rectangle:")),int(input("Enter width of Rectangle")))
print("Area of Rectangle:",re.area())
print("Perimeter of Rectangle:",re.perimeter())

class square(Shape):
    def __init__(self,length1):
        self.length1 = length1
    def area(self):
        return self.length1 * self.length1
    def volume(self):
        return self.length1 **3
    
s = square(int(input("Enter length1 of Square:")))
print("Area of Square:",s.area()) 
print("Volume of Square",s.volume())

class Rhombus(Shape):
    def __init__(self,d1,d2):
        self.d1 = d1
        self.d2 = d2
    def area(self):
        return (self.d1 * self.d2)/2
    
rh = Rhombus(int(input("Enter d1 of rhobus:")),int(input("Enter d2 of rhombus:")))
print("Area of Rhombus:",rh.area())    
rh.display()

