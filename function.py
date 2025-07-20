#understanding the python function
""" def painter():
    print("painter")
painter() """

#1.Create a function called add(),mul(),sub(), div() And get the input for a and b inside every
#Function then print the result
""" def add():
    print("addition")
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a+b)

def sub():
    print("subtraction")
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a-b)

def mul():
    print("multiplication")
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a*b)

def div():
    print("division")
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a/b)

add()
sub()
mul()
div() """

#2) Get a integer number from user and pass it to the function called findevenorodd().
#Let the futFtion print whether the number is even or odd.
""" def findevenorodd():
    if(num%2==0):
        print("even")
    else:
        print("odd")

 
num=int(input("enter the number:"))
findevenorodd() """


def painter(msg):
    print("message:",msg)

painter("helo")

