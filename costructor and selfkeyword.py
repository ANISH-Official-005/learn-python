#here the __init__ is a inbuilt function and it is a constructor 
#it automatically get worked wnen a object is just entered into the class
""" class laptop():
    def __init__(self):
        self.price=0
        self.gb="8gb"
    def display(self):
        print("display")

hp=laptop()
print(hp.price) """




#understanding the working of self
""" class laptop():
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("ram:",self.ram)
        print("processor:",self.processor)

hp=laptop()
dell= laptop()

hp.ram="8 gb"
hp.processor="i9"

dell.ram="16 gb"
dell.processor="i11"

hp.display()
dell.display() """











