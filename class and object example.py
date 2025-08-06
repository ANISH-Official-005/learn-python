#1. create a class called student create a variable= name and register number using constructor. 
#create a function called display which should display the name and register number of the student.

""" class student:
    def __init__(self):
        self.Name=""
        self.regno=0
    def display(self):
        print("name:",self.Name)
        print("regno:",self.regno)

hp=student()
hp.Name="anish"
hp.regno=962323243007

hp.display()  """

#understanding the concept 
""" class student:
    def __init__(self):
        self.Name="anish"
        self.regno="123"
    def display(self):
        print("name:",self.Name)
        print("regno:",self.regno)

hp=student()
hp.Name="supreme"
print(hp.Name)
print(hp.regno)
hp.display()  """

#2. create a class called fruit . create a variable called color using _init_ method. create a object called apple "pass the
#color variable as a parameter through object.

""" class fruit:
    def __init__(self, col):
        self.color=col


apple=fruit("red")
print(apple.color) """

 #3. create a class called teacher 
 #create a variable = name and register number using constructor
 #create a function called display which should display the name and register number of the teacher.

""" class teacher:
    def __init__(self,Name,n):
        self.name=Name
        self.regno=n
    def display(self):
        print("name:",self.name)
        print("regno:",self.regno)

t1=teacher("anish",1)
t2=teacher("abi",2)
t1.display()
t2.display() """

#create a class called calculator
#create 2 variables a and b
#reate a function called add, sub, mul, div all functions should take 2 variables as 
#parameter.
#pass the a and b value through object().

class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mul(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)
    

m1 = calculator(10,5)
m1.add()
m1.sub()
m1.mul()
m1.div()