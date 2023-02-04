
a=100
b=0
try:#u r telling this may have error, u try
    print(a/b)
    
#except Exception: #u saying if eror there i handle
#print("Cant divide any number by zero")

except Exception as e:
    print("Please note, number cant be divided by zero", e)

#to check your prg execution goes till end or get
print("Bye")


#whenever u open a file make sure u close it
#file may be anything - prg, database... gives clas
a=10
b=0
try:
    print("resoure open")
    print(a/b)

except Exception as e:
    print("Dont give second no as zero",e)

finally:
    print("Resource closed")


#like specialised doctors
#for those specific error only those exception
#blocks will get executed

a=10
try:
    b=int(input("Enter the number: "))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("please note, number cant be divided by zero",e)

except ValueError as e:
    print("Invalid input",e)
except Exception as e: #if not any above errors
    print("other error",e)
finally:
    print("Resource closed")



#raise used to interrupt normal prg flow and raise
#Example 1:

try:
    raise NameError("Hello friend")
except NameError:
    print("There is exception")

#2
x=10
if x%2!=0:
    raise Exception("x should be even number")
else:
    print("x is even number...correct")


class computer:             #class definition
    def config(self):       #config is a function
        print("Yes")

lenova=computer()           #object 1
lenova.config()

dell=computer()             #object 2
dell.config()


class Employee:
    def __init__(self,name, id):
        self.id=id
        self.name = name
    def display(self):
        print("ID: %d \nName: %s" % (self.id,self.name))

emp1=Employee("Naajir", 101)
emp2=Employee("Poornima", 102)

emp1.display()
emp2.display()



#variables and var.access in class and method
class computer():
    a=10
    b=20
    print("class variable inside class",a)

    def config(self): #config is a fuction
        c=100
        print("Yes")
        print("Instance access",self.b)

lenova=computer() #obect 1
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()
print("dell",dell.a)
lenova.config()
'''
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''

#PROJECT-1-QUIZ GAME
q1="""Who is your fav. Crush?
a.Priya
b.Anushka
c.Rashmika
d.samantha"""

q2="""What is your fav. sport?
a.badminton
b.kabaddi
c.cricket
d.khokho
"""

q3="""Who is your fav. character?
a.IronMan
b.Thor
C.Spiderman
d.Aquaman
"""

q4="""What is your fav. Bike?
a.Duke 390
b.Benelli900i
c.Kawasaki z900
d.Hayabusa
"""

q5="""what is your fav. car?
a.Audi A3
b.RollsRoyce
c.FordMustang
d.impala
"""

questions={q1:"a",q2:"c",q3:"b",q4:"c",q5:"d",}

name=input("Hi whats your name")
print("Hello",name,"Welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this ques(yes\no)")
    if flag1=="Yes":
        continue
    ans=input("enter your answer")
    if ans==questions[i]:
        print("Wow! You got one point")
        score=score+1
        print("Your current score is: ",score)
    else:
        print("Wrong answer, U lost 1 mark")
        score=score-1
        print("UR current score is: ",score)
        flag2=input("Do you want to Quit? type (yes/no)")
        if flag2=="yes":
            break
        print("Your total score is ",score)


#PROJECT-2-TIMER-CLOCK


import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer)
        time.sleep(1)
        t-=1
    print("FINISHED")
t=input("Enter the time in seconds: ")
countdown(int(t))



#PRJOJECT-3-FLAMES

name1=input("Enter the name1: ").lower()
name2=input("Enter the name2: ").lower()

name1=name1.replace(" ","")
name2=name2.replace(" ","")
print(name1)
print(name2)

for i in name1:
    for j in name2:
        if i==j:
            name1=name1.replace(i,"",1)
            name2=name2.replace(j,"",1)
            break
count=len(name1+name2)

print(count)
if count>0:
    list1=["Friends","Lovers","Affectionate","Marriage","Enemies","Siblings"]
    while len(list1
              )>1:
        c=count%len(list1)
        s_index=c-1

#slicing

        if s_index>=0:
            left=list1[:s_index]
            right=list1[s_index+1:]
            list1=right+left
        else:
            list1=list1[:len(list1)-1]
    print("Relationship:",list1[0])

else:
    print("Enter different names")
