#understanding the class and object
""" class goa():
    drink=""
    def party(self):
        print("enjoy the party")
    def museum(self):
        print("visit the museum")

ramesh=goa()
suresh=goa()

ramesh.party()
suresh.museum() """

#class and object accessing
""" class goa:
    name=""
    drink=""
    def party(self) :
     print("Lets Party.....")
    def beach(self) :
     print("Enjoying the beach")

ramesh=goa()
suresh=goa()

ramesh.name="Ramesh"
suresh.name="Suresh "

ramesh.drink="Yes"
suresh.drink="No"

print (ramesh.name)
print ("drink:",ramesh.drink)
print (suresh.name)
print ("drink:",suresh. drink)

ramesh.party()
suresh.beach() """

#1. create a class called laptop and create a following variables and functions.
#variables - Price,Processor,Ram
#Create Object - HP, DELL, LENOVO
class laptop:
    Price=0
    Processor=""
    Ram=""

hp=laptop()
Dell=laptop()
lenovo=laptop()

hp.price=20000
Dell.Price=25000
lenovo.price=23000

hp.Processor="amd ryzen3"
Dell.Processor="intel i3"
lenovo.Processor="intel i3"

hp.Ram=126
Dell.Ram=258
lenovo.Ram=512

print(hp.price)
print(Dell.Price)
print(lenovo.price)
print(hp.Processor)
print(Dell.Processor)
print(lenovo.Processor)
print(hp.Ram)
print(Dell.Ram)
print(lenovo.Ram)