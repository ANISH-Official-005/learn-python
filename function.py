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
#Let the function print whether the number is even or odd.
""" def findevenorodd(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")

 
a=int(input("enter a number:"))
findevenorodd(a)  """

#understanding purpose
""" def even(b):
    print("message",b)

a="hello"
even(a)
 """

#3) Get a integer number from user and pass it to the function called findpassorfail()
#Let the function print equalto or above 35 is pass and below 35 is fail.


""" def findpassorfail(mark):
    if(mark>=35 and mark<=100):
        print("pass")
    elif(mark<35 and mark>=0):
        print("fail")
    else:
        print("enter a valid mark")

a=int(input("enter the mark:"))
findpassorfail(a) """



#understanding multiple variable in parameters
#4)Get input for a and b and pass it to the function called printrange() 
#let the function print numbers from a to b.

""" def printrange(a,b):
    for i in range(a,b+1):
        print(i)


a=int(input("enter a:"))
b=int(input("enter b:"))
printrange(a,b) """

