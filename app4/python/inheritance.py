class human:
    def __init__(self,num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
# without using opp consept        
# class female:
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print("i can work") 
         

# using inheritance :::: purpose is to reusability of code and reduce code & coplexity    
class male(human):            
    pass # no any exta then pass

class female(human):
    def cook(self): # you can also add exta function
        print("i can cook")
    def work(self):
        return super().work()
class me(human):
    def __init__(self,name,heart):# parameter name can be diff
        super().__init__(heart) #use super class to access parent
        self.name = name
    def work(self):
        print("i can code ") # overriding consept
    def display(self):
        print(f"hi, i m {self.name} i have {self.num_heart} heart")
male1 = male(1) # no err bcz you gave a para value
male1.work()
print(male1.num_eyes)

# female1 = female() # error bcz of para value
# female1.eat()
# female1.cook()
# female1.work()

me_1 = me("frm",1) #must pass the value of parameter
print("name is " + me_1.name)
me_1.work()
print( me_1.num_eyes)
print(me_1.num_heart)
me_1.display()

                  