import random as r
x="i love sweets"
print(r.sample(x,2))

#EVERYTIME IT GIVES DIFFERENT OUTPUT
a=[1,2,3,4,5,6]

r.shuffle(a)
print(a)

a=[1,2,3,4,5,6]
print(r.choice(a))

b="welcome back"
print(r.choice(b))

a=r.random()
print(a)
#will return random numbers between 0.0 to 1.0
#0.0 includes 1.0 excludes
print(r.randint(20,30))

a=[10,20,30,40,50]
print(r.choices(a,k=10))


s="Hello good day"
print(r.choices(s,k=3))

print(r.uniform(5,10))
#returns any random number
#between the range include the
#range values
#float values'''


#to find all the functions available in particular modulekxz
z=dir(R)
print(z)

import calendar

print("Full calendar")
print(calendar.calendar(2022

print("particular Month")
print(calendar.month(2021,3))

print("set first day of the week")
calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.month(2021,12))

#prg - display date time

import datetime

a=datetime.datetime.now()
print(a)

sv=a.strftime("%y")#lowercase
fv=a.strftime("%y")#uppercase

print("year short version",sv)
print("year full version",fv)

def sample():
    print("great day")
    print("happy time")


sample() #CALL:
print("today")
sample()


#multiplication using function
def multi():
    n1=int(input("Number"))#without arg without return value
    n2=int(input("Number"))
    n3=int(input("Number"))
    prod=n1*n2*n3
    print(prod)
multi()

#multiplication using function
def multi():
    n1=int(input("Number"))#without arg with return value
    n2=int(input("Number"))
    n3=int(input("Number"))
    prod=n1*n2*n3
    return prod

res=multi()
print(res)

#with arguement without return value
#static input
def multi(n1,n2,n3):
  prod=n1*n2*n3
  print(prod)

multi(3,4,5)


#user input
def multi(a,b,c):
    prod=a*b*c
    print(prod)
n1=int(input("Enter 1: "))
n2=int(input("Enter 2: "))
n3=int(input("Enter 3: "))
multi(n1,n2,n3)


#with arguement with return value
#static input

def multi(n1,n2,n3):
  prod=n1*n2*n3
  return(prod)

res=multi(3,4,5)
print(res)'''

'''#userinput
def multi(a,b,c):
    prod=a*b*c
    return(prod)
n1=int(input("Enter 1: "))
n2=int(input("Enter 2: "))
n3=int(input("Enter 3: "))
res1=multi(n1,n2,n3)
print(res1)

#without argument and without return
def lemon():
   a=int(input("enter number:"))
   b=int(input("enter number:"))
   c=int(input("enter number:"))
   s=0
   s=a+b+c
   if(s<21):
       print("The lemons exceed the limit:",s-21)
   elif(s<21):
        print("The lemons are less",21-s)
   else:
      print("The lemons are sufficient")
lemon()
   

#MULTIPLICATION
def multi_table(n):
    for i in range(1,11):
        print(i,"x",n,"=",i*n)
n=int(input("which table"))
multi_table(n)

#sum of digits
def digits(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
        return sum
n=int(input("enter the number"))
res=digits(n)
print(res)

#FACTORS
def factors(n):
     for i in range(1,n+1):
         if n%i==0:
             print(i)
n=int(input("enter Number:"))
factors(n)
            
#Recursive function

def display():
    n=int(input("Enter a number"))
    if n==1:
           display()
    else:
        print("over")
display()

#Recursive function
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

result=fact(5)
print(result)

n=int(input("Enter Number:"))
a=0
b=1
sum = 0
count = 1

while(count <= n):
    print(sum, end =' ')
    count += 1
    a=b
    b=sum
    sum=a+b

def add_sub(x,y):
    sub=x-y
    add=x+y
    return sub,add

res1,res2=add_sub(20,10)
print(res1)
print(res2)

#variable length method
def sum(*a):
    c=0
    for i in a:
        c=c+1
    print(c)
sum(10,2,3,1,2)

i=10
while True:
    i=11
    print("Inside",i)
    break
print("outside",i)

def neon(n):
    sum=0
    sq=n*n
    while (sq!=0):
      s=sq%10
      sum=sum+s
      sq=sq//10
    if sum==n:
        print("neon")
    else:
        print("not a neon")
a=int(input("enter a:"))
neon(a)

      
