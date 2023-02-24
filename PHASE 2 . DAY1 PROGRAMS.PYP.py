#ANONYMOUS FUNCTION

L=[1,2,3]

r=map(lambda x:x+x,L)

print(list(r))

#map= helps to create iteratation

res=map(lambda n:pow(n,2),L)
print(list(res))

name="sam"
(lambda name:print(name))(name)

#write a program after creating a list  with even numbers with in the range 1 to 15,now apply lambda function and create a new list which should have square roots of the elements

from math import sqrt
L=(2,4,6,8,10,12,14)
r=map(lambda n:sqrt(n),L)
print(list(r))

class abstractdemo(ABC):
    @abstractmethod  #called decorator to
    #make the method(function) abstract one
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
#changing abstract to concrete
class demo(abstractdemo):
    def display(self) :
        print("Abstraction method")
    def show(self):
        print("2nd function")
obj=demo()
obj.display()
obj.show()

#one parent  and one child class

class parent :    #Base class
    def display(self):
        print("parent class")

#two classes -one child -like mom,dad ---ch1)
#inherits properties of mom and dad
class mom:
   def mdisplay(self) :
        print("mom class")
class dad:
    def ddisplay(self) :
        print("dad class")
class child(mom,dad):
    def cdisplay(self):
        print ("child class")
c1=child()
c1.cdisplay()
c1.mdisplay()
c1.ddisplay()
    



#DERIVED CLASS
class child(parent):  #child inherits property 
    def show(self):
        print("child class")

c=child()   #c is object for child class 
c.display()
c.show()

class A:
    n=30

class B(A):
    def calc (self):
        c=self.n+70
        print(c)

obj=B()
obj.calc()

#one parent and one child class
class grandparent :
    def display(self) :
        print ("grand parent class")
class parent(grandparent):
    def show(self):
        print("parent class")
class child(parent) :
    def printing(self):
        print("child class")
c=child()
c.display()
c.show()
c.printing

# one base class and multiple child class
#objects should be  created for child class individual
class parent :
    def pdisplay(self) :
        print("parent class")
class child1(parent) :
    def C1show(self):
        print("child class")
class child2(parent) :
    def c2show(self):
        print("child2 class")
c1=child1()
c1.c1show()
c1.pdisplay()
c2=child2()
c2.c2show()
c2.display()


class parent:
    def pdisplay(self) :
        print("parent class")
class child1(parent):
    def c1show(self) :
        print("child1")
class child2(parent):
    def c2show(self):
        print("child2")
class kid1(child1):
    def k1display(self):
        print("kid1 class")
class kid2(child1):
    def k2display(self):
        print("kid2 class")
class kidd1(child2):
    def k1show(self):
        print("kidd1 class")
class kidd2(child2):
    def k2show(self):
        print("kidd2 class")
c1=kid1()
c1.k1display()
c1.c1show()
c1.pdisplay()
c2=kid2()
c2.k2display()
c2.c1show()
c2.pdisplay()
c2.c1show()
c2.pdisplay()
c3=kidd1()
c3.k1show()
c3.c2show()
c3.pdisplay()
c4=kidd2()
c4.k2show()
c4.c2show()
c4.pdisplay()'''

n=int(input("enter the num:"))
while(n>=10):
    s=0
    for i in range(0,len(str(n))+1):
        r=n%10
        s=s+r**2
        n=n//10
    n=s
if n==1:
    print("happy number")
else:
    print("Not a happy number")

    


