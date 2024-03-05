#inheretance
class Father:
    name = ""
    
    def property(self):
        return "I have 15 acres of property"
    
    
class Child(Father):
    def child_property(self):
        return "I own 5 acres of property"
        
class GrandChild(Child):
    def grand_child_property(self):
        return "He or She owns 1 acres of property"
a = Child()
print(a.property())
a.name = "Roopesh"
print(a.name)
print(a.child_property())

f = Father()
print(f.property())

g = GrandChild()
print(g.property())
print(g.child_property())

#TYPE 1 : SINGLE INHERETANCE
class Parent:
      def func1(self):
           print("this is function one")
class Child(Parent):
      def func2(self):
            print(" this is function 2 ")
ob = Child()
ob.func1()
ob.func2()


#TYPE 2 : MULTIPLE INHERETANCE

class Parent:
     def func1(self):
         print("this is function 1")
class Parent2:
     def func2(self):
           print("this is function 2")
class Child(Parent , Parent2):
     def func3(self):
          print("this is function 3")
ob = Child()
ob.func1()
ob.func2()
ob.func3()


# TYPE 3 : Multilevel Inheritance

class Parent:
      def func1(self):
           print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Child):
      def func3(self):
          print("this is function 3")
ob = Child2()
ob.func1()
ob.func2()
ob.func3()
      

#TYPE 4 : Hierarchical Inheritance
class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Parent):
     def func3(self):
         print("this is function 3")
ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()


#TYPE 5: Hybrid Inheritance

class Parent:
      def func1(self):
          print("this is function one")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child1(Parent):
      def func3(self):
          print(" this is function 3")
class Child3(Child , Child1):
      def func4(self):
          print(" this is function 4")
ob = Child3()
ob.func1()