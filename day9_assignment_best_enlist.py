#1.write a python program to loop through a list of numbers and add +2 to every value to elements in list 
list1=[1,2,3,4,5]
print("list1 is: ",list1)
for i in range(len(list1)):
    list1[i]=list1[i]+2
print("After adding 2 to every elements in list1: ",list1)
print()

#2.write a program to get the below pattern
#   54321
#   4321
#   321
#   21
#   1
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()
print()

#3.python program to print the fibonacci sequence
def fibonacci(n):
    n1,n2=0,1
    c=0
    if n<0:
        print("Please Enter positive integer")
    if n==0 or n==1:
        return(n)
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
s=int(input("Enter the number for fibonaaci sequence: "))
print('The fibonacci sequence for %d integers is: '%s)
for i in range(s):
    print(fibonacci(i))
print()

#4.explain Armstrong number and write a code with function
print("Armstrong number is a number that forms total of the same number when each digits is raised to the power of the number of digits in the number")
def armstrong(n):
    sum=0
    while(n>0):
        unitdigit=n%10
        sum+=unitdigit**order
        n=n//10
    return sum
n=int(input("Enter the number to check whether it is an Armstrong number: "))
order=len(str(n))
arm=armstrong(n)
if arm==n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")
print()

#5.write a program to print multiplication table of 9
for i in range(1,11):
    print("9 x %d = %d"%(i,(i*9)))
print()

#6.check if a program is negative or positive
posorneg=int(input("Enter the integer to check if it is positive or negative: "))
if posorneg>=0:
    print(posorneg,"is positive")
else:
    print(posorneg,"is negative")
print()

#7.write a python program to convert the number of days to ages
days=int(input("Enter the no. of days: "))
ages=days//365
print("The age is ",ages)
print()

#8.solve trigonometry problem with math function, write a program to solve using math function
import math
def trigonometry(a,b):
    if a=='sin':
        return math.sin(b)
    elif a=='cos':
        return math.cos(b)
    elif a=='tan':
        return math.tan(b)
    else:
        return "invalid input"
a=input("Enter the trigonometric function: ")
b=int(input("Enter the theta value: "))
print(trigonometry(a,b))
print()

#9.create a basic calculator by using if condition
def calculator(x,y,z):
    if x=='add':
        return y+z
    elif x=='sub':
        return y-z
    elif x=='mul':
        return y*z
    elif x=='div':
        return y/z
    elif x=='expo':
        return y**z
    else:
        return "Invaid input"
x=input("Enter the basic operation: ")
y=int(input("Enter the first number: "))
z=int(input("Enter the second nuumber: "))
print("The answer is: ",calculator(x,y,z))



    
