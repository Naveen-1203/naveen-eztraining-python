n1,n2=int(input("Enter no1:")),int(input("Enter no2:"))
bAnd=n1 & n2
bor=n1|n2
bxor=n1^n2
print(bAnd)
print(bor)
print(bxor)



n=int(input("Enter a number:"))
if(n==500):
    print("The number is 500")
else:
    print("The number is not 500")


n=int(input("Enter a number:"))
if(n%11==0):
    print("number is divisible by 11")
else:
    print("number is not divisible by 11")


i=1
while(i<=30):
    print(i)
    i=i+2

i=2
while(i<=20):
    print(i)
    i=i+2


n=int(input("Enter a number:"))
if(n%2==0)&(n>0):
      print("The number is even-positive")
elif((n%2==0)&(n<0)):
      print("The number is even-negative")
elif((n%2!=0)&(n>0)):
      print("The number is odd-positive")
elif((n%2!=0)&s(n<0)):
      print("The number is even-positive")
else:
    print("The number is neither odd nor even")


i=1
while(i<=30):
    print(i)
    i=i+2


n=10.3
res=n-int(n)
if res!=0:
    print("float")
else:
    print("integer")


a,b,c=int(input("Enter a:")),int(input("Enter b:")),int(input("Enter c:"))
if(a>b and a>c):
    print("a is greater")
elif(b>a and b>c):
    print("b is greater")
else:
    print("c is greater")


n1,n2=int(input("Enter no1:")),int(input("Enter no2:"))
if(n1>n2):
    print("n1 is greater")
else:
    print("n2 is greater:")

n=20
if n==int(n):
   print("It is a integer")
else n==float(n):
    print("It is floating number")



n=30
if isinstance(n,float)==True:
    print("The number is a floating number")
else:
    print("The number is a integer number")
    

n=25
if n%1==0:
    print("It is a integer")
else:
    print("It is a floating number")



a=list(map(int,input("Numbers:").split()))
print(a)


import random
n = random.randrange(1,50)
guess=int(input("Enter any number:"))
while n!=guess:
    if guess<n:
        print("Too low")
        guess =int(input("Enter number again:"))
    elif guess>n:
        print("Too high")
        guess =int(input("Enter number again:"))
    else:
        break
print("you guessed it right")



print("its",'a','good','day',end=' ')

print("all",'is','good',sep='#*#',end=' ')

print("Joy")


t=int(input("enter temperature:"))
if t>45:
    print("hottest")
elif t>=40 and t<45:
    print("hot")
elif t>=25 and t<40:
    print("moderate")
elif t>=10 and t<25:
    print("cold")
else:
    print("chill")


i=1
while(i<=10):
    print(i)
    i=i+1
