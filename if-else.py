""" if (False):
    print("yes")
else:
    print("no") """
""" 
print('win'=='wina') """

""" 
rcb="lose"
if(rcb=="win"):
    print("Ee Sala Cup Namade")
else:
    print("lollipop") """



""" meghna=input()
if(meghna=="Died"):
    print("surya meets priya")
else:
    print("surya weds meghna") """

""" mark=int(input("enter the mark:"))
if(mark>35):
    print("pass")
else:
    print("fail") """
""" 

income=int(input("enter the income:"))
if(income>7000):
    print("scholarship is available")
else:
    print("not eligible") """



""" a=int(input("enter the number:"))
if (a%3==0 and a%5==0):
    print("divisible ")
else:
    print("not divisible") """


""" name="anish"
age=19
print("the name is" + name ) """

""" number=int(input("enter the number:"))
if(number%2==0):
    print("even")
else:
    print("odd") """

#elif concept
""" score=int(input("enter the number:"))
if(score<35):
    print("poor student")
elif(score>35 and score<70):
    print("average student")
else:
    print("good student")
 """

""" a=int(input("number1:"))
b=int(input("number2:"))
user=input("add/sub/mul/div:")
if(user=="add"):
    print(a+b)
elif(user=='sub'):
    print(a-b)
elif(user=='mul'):
    print(a*b)
elif(user=='div'):
    print(a/b)
else:
    print("invalid operation") 
"""


#performing operations under if-else
""" score_percent=int(input("enter the score:"))
if(score_percent>70):
    name=input("enter the name:")    
    dept=input("enter the dept:")
    locn=input("enter the location:")
    print('you are eligible')
else:
    print("not elgible") """

#nested if-else concept
""" salary=int(input("enter the salary:"))
age=int(input("enter the age:"))
if(salary>=20000 or age<=25):
    req_lnat=int(input("enter the amount"))
    if(req_lnat<=50000):
       print("eligible for loan")
    else:
       print("maximum loan amount is 50000")
else:
    print("not eligible for loan") """


a=int(input("enter the a:"))
b=int(input("enter the b:"))
c=int(input("enter the c:"))
d=int(input("enter the d:"))
e=int(input("enter the e:"))
add=a+b+c+d+e
print(add)
avg=add/5
print(avg)
if(avg<35):
    print("additional class is required")
else:
    print("you are good to go")