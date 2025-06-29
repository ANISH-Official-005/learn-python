# introductionn of for loop

""" for i in range(1,11):
    print(i,"x2=", i*2)
 """

""" a=1
b=33
print(a,b) """



""" a=int(input("enter a:"))
b=int(input("enter b:"))
for i in range(a+1,b):
    print(i) """


# counting concept
#count the odd numbers between 1 and 10 
""" count=0
for i in range(1,11):
    if(i%2!=0):
        count=count+1
print("count:",count) """


# count the even and odd numbers between 1 and 10
""" count_even=0
count_odd=0
for i in range(1,11):
    if(i%2==0):
        count_even=count_even+1
    elif(i%2!=0):
        count_odd=count_odd+1
    else:
        print("no count")
print("even:",count_even)
print("odd:",count_odd) """


#count the number which are divisible by 3 and 5.
#range 1-100.
""" count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print("no divisible by 3 and 5 within range 1-100:",count) """

#write a program to compute the sum of the first 5 natural numbers.
""" sum=0
for i in range(1,6):
    sum=sum+i
print("the sum of first 5 natural numbers is:",sum) """

#for loop with list concept

#write a program to read 10 numbers from the keyboard and find their sum and average

""" lst=[]
for i in range(5):
    num=input("enter the number"+str(i+1))
    lst.append(int(num))
print(lst)

sum=0
for i in lst:
    sum=sum+i
print(sum)
avg=sum/len(lst)
print(avg) """

#write a program to display n terms of natural numbers and their sum (Test data:7)
""" a=[]
n=int(input("enter the number:"))
for i in range(n):
      b=i+1
      a.append(b)
print("the first",n,"natural number is:",a)
sum=0
for _ in a:
      sum=sum+_
print("the sum of first",n,"natural number is:",sum) """

#write a program to display the cube of the number up to an integer

""" n=int(input("enter the number:"))
for i in range(n):
    b=i+1
    cube=b*b*b
    print("number is:",b,"and cube of the",b,"is:",cube ) """