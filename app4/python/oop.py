# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def pass_or_fail(self):
#         if self.marks >= 40:
#             return "Pass"
#         else:
#             return "Fail"
        
# student1 = Student("Yogesh", 85)
# print(student1.pass_or_fail())

# student2 = Student("Anand", 30)
# print(student2.pass_or_fail())



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"The name is {self.name} and his or her age is {self.age}"

person1 = Person("Yogesh", 24)
print(person1.say_hello())


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Main function
def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter operation (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input")

# Run the calculator
calculator()
