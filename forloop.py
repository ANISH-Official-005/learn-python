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
