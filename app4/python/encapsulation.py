# class BaseClass:
#     def __init__(self):
#         print("This is data of base class")
#         self.a = "Pranshtech"
#         self._b = "Pranshtech"
    
# class DerivedClass:
#     def __init__(self):
#         print("This is data of derived class")
#         BaseClass.__init__(self)
#         print(self._b)
    
    
# d = DerivedClass()
# print(d.a)

# b = BaseClass()
# print(b.a)
# print(b._b)

#1> public

# class base:
#   def __init__(self):
#     self.a = "foram"

# class derive(base):
#   def __init__(self):
#     base.__init__(self)
    
# obj1 = base()
# print(obj1.a)
# obj2 = derive()
# print(obj2.a)


#2> protected

# class base:
#   def __init__(self):
#     self._a = "foram"

# class derive(base):
#   def __init__(self):
#     base.__init__(self)

# obj1 = base()
# print(obj1._a)
# obj2 = derive()
# print(obj2._a)

#3> private : error bcz of private can't be accessed outside the class
# class base:
#   def __init__(self):
#     self.__a = "foram"

# class derive(base):
#   def __init__(self):
#     base.__init__(self)

# obj1 = base()
# print(obj1.__a)
# obj2 = derive() 
# print(obj2.__a)






