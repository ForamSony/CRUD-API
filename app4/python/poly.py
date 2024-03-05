#type 2 of poly:
#1>compile time:i,ii   
#i>method overloading (same func name in 1 class,not suported) arg not same in func
# class add:
#     def sum (self,a,b):
#       return a+b 

#     def sum (self,a):
#       return a       
# sum1 = add()
# print(sum1.sum(3,4))
# print(sum1.sum(3))
# not supported in python

#ii> method overriding (same func name in diff class) arg same in func
# class Poly:
#     def add(self, a, b):
#         print(a+b)
#         return a + b
    
# class Child(Poly):
#     def add(self, a , b):
#         print(a*b)
#         return a * b
    
# p = Poly()
# c = Child()
# p.add(5,4)
# c.add(3,5)


# 2> runtime: 

# i>virtual function 


#Create a base class "Shape" with a method calculate_area(). Then, create two derived classes "Circle" and "Rectangle," each overriding the calculate_area() method. Finally, demonstrate polymorphism by calling calculate_area() on instances of both classes.


